# main.py
from src.component.data_ingestion import DataIngestion
from src.component.data_transformation import DataTransformation
from src.component.model_trainer import ModelTrainer


if __name__ == "__main__":
    # ingestion = DataIngestion()
    # train_path, test_path = ingestion.initiate_data_ingestion()
    # print(f"✅ Data Ingestion Completed!")
    # print(f"📁 Train file: {train_path}")
    # print(f"📁 Test file: {test_path}")

    transformer = DataTransformation()
    X_train, X_test, y_train, y_test = transformer.initiate_data_transformation(
    train_path="artifacts/train.csv",
    test_path="artifacts/test.csv")
    print(f'data tranformation completed')
    

    data_transformation = DataTransformation()
    X_train, X_test, y_train, y_test = data_transformation.initiate_data_transformation("artifacts/train.csv", "artifacts/test.csv")

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(X_train, X_test, y_train, y_test)



