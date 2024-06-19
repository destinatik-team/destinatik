# Destinatik Model

## Sumber Dataset
Dataset source: https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination/data

## Model Description:
- Cleaning the data (including dropping unused columns)
- preprocessing
- modelling with RecommenderNet with editing
- recommendation output
All the steps bellow based on: https://keras.io/examples/structured_data/collaborative_filtering_movielens/

## File Model Destinatik:
[Collaborative_Filtering_Destinatik](https://github.com/destinatik-team/destinatik/blob/ml-path/Collaborative_Filtering_Destinatik.ipynb)

## File Model Saved (tf.keras.Model.save())
[destinatik_model.h5](https://github.com/destinatik-team/destinatik/blob/ml-path/destinatik_model_v3.h5)

## File Model Export (tf.saved_model())
[destinatik_model_tfjs](https://github.com/destinatik-team/destinatik/tree/ml-path/destinatik_model_tfjs)

## File tfjs export converted (tensorflowjs converter)
[export_tfjs](https://github.com/destinatik-team/destinatik/tree/ml-path/export_tfjs)