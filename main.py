import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from flask import Flask, request, jsonify
import gdown
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

app = Flask(__name__)


url = "https://drive.google.com/file/d/1dJ6sHWOsBa2XoJlzlUnwSHV0LUYsk20Y/view?usp=drive_link"
output = 'model.h5'
gdown.download(url, output)


class RecommenderNet(keras.Model):
    def __init__(self, num_users, num_places, embedding_size, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.num_users = num_users
        self.num_places = num_places
        self.embedding_size = embedding_size
        self.user_embedding = layers.Embedding(
            num_users,
            embedding_size,
            embeddings_initializer="he_normal",
            embeddings_regularizer=keras.regularizers.l2(1e-6),
        )
        self.user_bias = layers.Embedding(num_users, 1)
        self.place_embedding = layers.Embedding(
            num_places,
            embedding_size,
            embeddings_initializer="he_normal",
            embeddings_regularizer=keras.regularizers.l2(1e-6),
        )
        self.place_bias = layers.Embedding(num_places, 1)

    def call(self, inputs):
        user_vector = self.user_embedding(inputs[:, 0])
        user_bias = self.user_bias(inputs[:, 0])
        place_vector = self.place_embedding(inputs[:, 1])
        place_bias = self.place_bias(inputs[:, 1])

        dot_user_place = tf.tensordot(user_vector, place_vector, 2)
        x = dot_user_place + user_bias + place_bias
        return tf.nn.relu(x)

    def get_config(self):
        config = super(RecommenderNet, self).get_config()
        config.update({
            'num_users': self.num_users,
            'num_places': self.num_places,
            'embedding_size': self.embedding_size
        })
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)

# Load the user and place encodings
tourism_rating_path = 'tourism_rating.csv'
tourism_with_id_path = 'tourism_with_id.csv'

rates = pd.read_csv(tourism_rating_path)
places = pd.read_csv(tourism_with_id_path)

user_ids = rates["User_Id"].unique().tolist()
place_ids = rates["Place_Id"].unique().tolist()

num_users = len(user_ids)
num_places = len(place_ids)
embedding_size = 50

user2user_encoded = {x: i for i, x in enumerate(user_ids)}
place2place_encoded = {x: i for i, x in enumerate(place_ids)}
place_encoded2place = {i: x for i, x in enumerate(place_ids)}

# Building the model
model = RecommenderNet(num_users, num_places, embedding_size)
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),
)

# Sample input to build the model (replace with actual data if available)
sample_inputs = np.array([[0, 0], [1, 1]])  # Example shape, replace with actual data shape
model(sample_inputs)  # Call the model to build it

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World'


@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        user_id = data.get('user_id')
        city = data.get('city')
        place_id = data.get('place_id')

        if not user_id and not city and not place_id:
            return jsonify({'error': 'Either user_id, city, or place_id must be provided'}), 400

        if user_id:
            if user_id not in user2user_encoded:
                return jsonify({'error': 'User ID not found'}), 400
            user_encoder = user2user_encoded[user_id]
            user_rated_places = rates[rates.User_Id == user_id].Place_Id.values
        else:
            user_encoder = 0  # Dummy user encoder for city-based recommendation
            user_rated_places = []

        if city:
            places_in_city = places[places['City'] == city]
            places_not_visited = places_in_city[~places_in_city["Place_Id"].isin(user_rated_places)]["Place_Id"]
        elif place_id:
            if place_id not in place2place_encoded:
                return jsonify({'error': 'Place ID not found'}), 400
            places_not_visited = [place_id]
        else:
            places_not_visited = places[~places["Place_Id"].isin(user_rated_places)]["Place_Id"]

        places_not_visited = list(
            set(places_not_visited).intersection(set(place2place_encoded.keys()))
        )
        places_not_visited = [[place2place_encoded.get(x)] for x in places_not_visited]

        if user_encoder == 0:
            user_place_array = np.array(places_not_visited)
        else:
            user_place_array = np.hstack(
                ([[user_encoder]] * len(places_not_visited), places_not_visited)
            )

        ratings = model.predict(user_place_array).flatten()
        top_ratings_indices = ratings.argsort()[-10:][::-1]
        recommended_place_ids = [
            place_encoded2place.get(places_not_visited[x][0]) for x in top_ratings_indices
        ]

        recommended_places = places[places["Place_Id"].isin(recommended_place_ids)]

        recommendations = []
        for row in recommended_places.itertuples():
            recommendations.append({"place_id": row.Place_Id, "place_name": row.Place_Name, "category": row.Category})

        return jsonify(recommendations), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
