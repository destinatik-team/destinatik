# Destinatik Model

## Dataset Source
Dataset source: https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination/data


## Model Description:
- Cleaning the data (including dropping unused columns, and removing duplicate data)
- Preprocessing (including one-hot encoding)
- Building the model using TensorFlow custom object (RecommenderNet)
- Recommendation output with expected value and model prediction result

All the steps bellow based on: https://keras.io/examples/structured_data/collaborative_filtering_movielens/


## Model Destinatik Source Code
This model was built by using a collaborative filtering method and the model code documentation is below:
[Collaborative_Filtering_Destinatik Source Code](https://github.com/destinatik-team/destinatik/blob/ml-path/Collaborative_Filtering_Destinatik.ipynb)


## Exported Model File
This model was saved:
- using `tf.keras.Model.save()` at [destinatik_model.h5](https://github.com/destinatik-team/destinatik/blob/ml-path/destinatik_model_v3.h5)
- using `tf.saved_model()` at [destinatik_model_tfjs](https://github.com/destinatik-team/destinatik/tree/ml-path/destinatik_model_tfjs)
- and using terminal `!tensorflowjs_converter --input_format=tf_saved_model --output_format=tfjs_graph_model destinatik_model_tfjs ./export_tfjs/` (tensorflowjs converter) [export_tfjs](https://github.com/destinatik-team/destinatik/tree/ml-path/export_tfjs)
