import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import joblib
from sklearn.preprocessing import LabelEncoder

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")
    label_encoder_path = os.path.join("artifacts", "label_encoder.pkl")
    

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function returns the preprocessing pipeline.
        '''
        try:
            numerical_features = [
                "Time_spent_Alone",
                "Social_event_attendance",
                "Going_outside",
                "Friends_circle_size",
                "Post_frequency"
            ]

            categorical_features = ['Stage_fear','Drained_after_socializing']

            numerical_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            categorical_pipeline = Pipeline(steps= [
                ('imputer', SimpleImputer(strategy= 'most_frequent')),
                ('one_hot_encoder', OneHotEncoder()),
                ('scaler',StandardScaler(with_mean= False))
            ])

            preprocessor = ColumnTransformer([
                ("num_pipeline", numerical_pipeline, numerical_features),
                ('cat_pipeline', categorical_pipeline, categorical_features)
            ])

            logging.info('Numerical columns standard scaler is completed')

            logging.info('Categorical columns encoding is completed')

            logging.info(f'Numerical columns :{numerical_features}')
            logging.info(f'categorical columns :{categorical_features}')

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data")

            target_column = "Personality"

            input_features_train = train_df.drop(columns=[target_column], axis=1)
            target_feature_train = train_df[target_column]

            input_features_test = test_df.drop(columns=[target_column], axis=1)
            target_feature_test = test_df[target_column]

            label_encoder = LabelEncoder()
            target_feature_train = label_encoder.fit_transform(target_feature_train)
            target_feature_test = label_encoder.transform(target_feature_test)

            preprocessor = self.get_data_transformer_object()

            logging.info("Fitting and transforming data...")

            X_train = preprocessor.fit_transform(input_features_train)
            X_test = preprocessor.transform(input_features_test)

            # Save the preprocessor
            save_object(
                file_path=self.config.preprocessor_obj_file_path,
                obj=preprocessor
            )
            save_object(file_path= self.config.label_encoder_path,
                        obj= label_encoder)


            return X_train, X_test, target_feature_train, target_feature_test

        except Exception as e:
            raise CustomException(e, sys)
