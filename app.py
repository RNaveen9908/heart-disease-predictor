from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class HeartData(BaseModel):
    age:int
    sex:int
    cp:int
    trestbps:int
    chol:int
    fbs:int
    restecg:int
    thalach:int
    exang:int
    oldpeak:float
    slope:int
    ca:int
    thal:int

@app.get("/")
def home():
    return {"message":"Heart Disease Prediction API"}

@app.post("/predict")
def predict(data: HeartData):

    df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(df)

    return {
        "prediction": int(prediction[0])
    }