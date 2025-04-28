from fastapi import FastAPI
from pydantic import BaseModel
from preprocessing import preprocess_input  # Import fungsi preprocessing
from prediction import predict_calories_burned  # Import fungsi prediksi

# Inisialisasi FastAPI
app = FastAPI(title="Calorie Burn Prediction API")

# Skema input
class InputData(BaseModel):
    BMI: float
    Age: int
    Gender: int
    Workout_Type_Cardio: int
    Workout_Type_Strength: int
    Workout_Type_HIIT: int
    Workout_Type_Yoga: int
    Experience_Level: int
    Session_Duration: float  # Session_Duration (hours)
    Max_BPM: int
    Avg_BPM: int
    Fat_Percentage: float

# Endpoint root
@app.get("/")
def read_root():
    return {"message": "Calorie Burn Prediction API is running"}

# Endpoint prediksi
@app.post("/predict")
def predict_calories_burned_endpoint(data: InputData):
    processed_data = preprocess_input(data)  # Panggil fungsi preprocessing
    prediction = predict_calories_burned(processed_data)  # Panggil fungsi prediksi
    return {"calories_burned": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)