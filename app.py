from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.logger import logging

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = CustomData(
        Time_spent_Alone=float(request.form['Time_spent_Alone']),
        Social_event_attendance=float(request.form['Social_event_attendance']),
        Going_outside=float(request.form['Going_outside']),
        Friends_circle_size=float(request.form['Friends_circle_size']),
        Post_frequency=float(request.form['Post_frequency']),
        Stage_fear=request.form['Stage_fear'],
        Drained_after_socializing=request.form['Drained_after_socializing']
    )

    df = data.get_data_as_dataframe()
    predictor = PredictPipeline()
    result = predictor.predict(df)[0]

   


    logging.info(f"You are likely an {result}")
    return render_template('index.html', prediction_text=f"You are likely an {result}")

if __name__ == "__main__":
    app.run(debug=True)
