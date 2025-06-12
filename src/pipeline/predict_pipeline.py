import os
import sys
import pandas as pd
import numpy as np
import dill

from src.exception import CustomException
from src.utils import load_object # We'll create this if needed


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            label_encoder_path = os.path.join("artifacts", "label_encoder.pkl")

            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)
            label_encoder = load_object(label_encoder_path)

            # Apply preprocessing
            data_scaled = preprocessor.transform(features)

            # Predict
            preds = model.predict(data_scaled)

            # Decode label (e.g. 0 → Introvert)
            final_preds = label_encoder.inverse_transform(preds)

            return final_preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(
        self,
        Time_spent_Alone,
        Social_event_attendance,
        Going_outside,
        Friends_circle_size,
        Post_frequency,
        Stage_fear,
        Drained_after_socializing
    ):
        self.Time_spent_Alone = Time_spent_Alone
        self.Social_event_attendance = Social_event_attendance
        self.Going_outside = Going_outside
        self.Friends_circle_size = Friends_circle_size
        self.Post_frequency = Post_frequency
        self.Stage_fear = Stage_fear
        self.Drained_after_socializing = Drained_after_socializing

    def get_data_as_dataframe(self):
        try:
            data_dict = {
                "Time_spent_Alone": [self.Time_spent_Alone],
                "Social_event_attendance": [self.Social_event_attendance],
                "Going_outside": [self.Going_outside],
                "Friends_circle_size": [self.Friends_circle_size],
                "Post_frequency": [self.Post_frequency],
                "Stage_fear": [self.Stage_fear],
                "Drained_after_socializing": [self.Drained_after_socializing],
            }

            return pd.DataFrame(data_dict)

        except Exception as e:
            raise CustomException(e, sys)
