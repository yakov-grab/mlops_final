from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import numpy as np


# Загрузите модель из файла pickle
with open('../models/model_titanic.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# Определение класса для данных о пассажире
class Passenger(BaseModel):
    Pclass: int         # Класс: 1, 2, 3
    Sex: str            # Пол: male, female
    Age: float          # Возраст
    SibSp: int          # Количество родственников (супруг+братья\сестры): 0, 1, 2, 3
    Parch: int          # Количество родственников (родители+дети): 0, 1, 2
    Fare: float         # Cтоимость билета

app = FastAPI()

@app.post("/predict/")
async def predict_survival(passenger: Passenger):
    X_new = np.array([[passenger.Pclass, passenger.Sex, passenger.Age, passenger.SibSp, passenger.Parch, passenger.Fare]])
    prediction = model.predict(X_new)
    return {"survival_prediction": int(prediction[0])}

