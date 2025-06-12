# 🧠 Introversion vs. Extroversion Personality Prediction

A machine learning web application that predicts whether a person is an **Introvert** or **Extrovert** based on their lifestyle and behavioral traits. Built using Python, Flask, and scikit-learn.

## 📊 Project Overview

This project aims to classify users into **Introvert** or **Extrovert** categories by analyzing features like:

- Time spent alone
- Social event attendance
- Frequency of going outside
- Size of friends circle
- Social media post frequency
- Stage fear
- Whether the user feels drained after socializing

It uses a trained classification model wrapped with a Flask interface for easy interaction.

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Flask** – Web framework
- **Pandas / NumPy** – Data handling
- **scikit-learn** – Machine Learning
- **dill** – Model serialization
- **HTML/CSS** – Frontend interface

---

## 🚀 Features

- Clean and responsive **Flask web UI**
- Data preprocessing with pipelines
- Encodes categorical data with `OneHotEncoder`
- Scales numerical features using `StandardScaler`
- Trained with various classifiers (e.g., SVC, Logistic Regression)
- Easily deployable and extendable

---

## 📁 Project Structure

inttroversion-extroversion-ml/
│
├── artifacts/ # Serialized model, preprocessor, label encoder
├── src/
│ ├── component/ # Data ingestion, transformation, training
│ ├── pipeline/ # CustomData class and prediction pipeline
│ ├── utils.py # save_object function, utilities
│ ├── logger.py # Logging configuration
│ └── exception.py # Custom exception handling
├── templates/
│ └── index.html # Frontend HTML form
├── app.py # Flask main app
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🧪 How to Use





```bash
### 1. Clone the Repository
git clone https://github.com/your-username/introvert-extrovert-ml.git
cd introvert-extrovert-ml


python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


### 2. Create & Activate Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Train the model(optional)
python main.py

### 5. Run the flask app 
python app.py
Open your browser and go to http://localhost:5000


```

🙏 Acknowledgements
Krish Naik – End to End machine learning tutorial

The Scikit-learn team for excellent documentation

The Python and Flask communities
