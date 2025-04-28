import pickle
import pandas as pd

# Load model
with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_calories_burned(data):
    # Lakukan prediksi menggunakan model yang sudah di-load
    prediction = model.predict(data)[0]
    return prediction