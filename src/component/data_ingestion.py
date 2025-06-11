import os
import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException
import sys

class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")

        try:
            # Read dataset from your local `data` folder
            df = pd.read_csv(os.path.join("data", "personality_dataset.csv"))
            logging.info("Dataset successfully loaded as DataFrame")

            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)
            df.to_csv(self.config.raw_data_path, index=False)

            # Train-test split
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

            train_df.to_csv(self.config.train_data_path, index=False)
            test_df.to_csv(self.config.test_data_path, index=False)

            logging.info("Train-test split done and saved in artifacts folder")

            return self.config.train_data_path, self.config.test_data_path, self.config.raw_data_path

        except Exception as e:
            logging.error("Exception occurred during data ingestion")
            raise CustomException(e, sys)
