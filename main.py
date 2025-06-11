# main.py
from src.component.data_ingestion import DataIngestion

if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()
    print(f"✅ Data Ingestion Completed!")
    print(f"📁 Train file: {train_path}")
    print(f"📁 Test file: {test_path}")
