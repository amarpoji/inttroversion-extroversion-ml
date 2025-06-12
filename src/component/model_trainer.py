import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import joblib

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object


@dataclass
class ModelTrainerConfig:
    model_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()
      
    def initiate_model_training(self, X_train, X_test, y_train, y_test):
        try:
            logging.info("Starting model training...")

            model = RandomForestClassifier()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred, average='weighted')

            logging.info(f"Model Accuracy: {acc}")
            logging.info(f"F1 Score: {f1}")
            logging.info(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")

            save_object(self.config.model_path, model)

            return acc, f1

        except Exception as e:
            raise CustomException(e, sys)

