import sys 
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException

if __name__ == "__main__":
    try:
        data = CustomData(
            Time_spent_Alone=1,
            Social_event_attendance=7,
            Going_outside=7,
            Friends_circle_size=7,
            Post_frequency=7,
            Stage_fear='No',
            Drained_after_socializing='No'
        )

        final_df = data.get_data_as_dataframe()

        predictor = PredictPipeline()
        prediction = predictor.predict(final_df)

        print("Personality Prediction:", prediction[0])

    except CustomException as e:
        print("Custom Exception:", e)
    except Exception as e:
        print("Unhandled Exception:", e)