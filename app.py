

#=============================StTART OF FAST API code==============================>

# app.py
import pickle
import numpy as np
import pandas as pd
import json
from fastapi import FastAPI
from pydantic import BaseModel


# Load model
# with open("model_log.pkl", "rb") as f:
with open("D:\ml-demo\model_log.pkl","rb") as f:
    model = pickle.load(f)

# Define input schema
class Passenger(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp:int
    Parch:int
    Fare: float
    Cabin:str
    Embarked:str


app = FastAPI(title="Titanic Survival Predictor")

@app.get("/")
def root():
    return {"message": "Titanic model API is running!"}

@app.post("/predict")
def predict(passenger: Passenger):

    
    data = [
        [
            passenger.Pclass, 
            passenger.Sex, 
            passenger.Age, 
            passenger.SibSp,
            passenger.Parch,
            passenger.Fare,
            passenger.Cabin,
            passenger.Embarked

         ]
        ]
    cols = ["Pclass","Sex","Age","SibSp","Parch","Fare","Cabin","Embarked"]
    df = pd.DataFrame(data,columns=cols)
    prediction = model.predict(df)
    survival = "Survived" if prediction == 1 else "Did not survive"
    return {"prediction": int(prediction), "result": survival}

# Set these below variable one by one on PS prompt
#     $jsonFilePath = "D:\ml-demo\fast-data.json"
#     $jsonContent = Get-Content -Path $jsonFilePath -Raw
#     $dataObject = $jsonContent | ConvertFrom-Json
#     $body = $dataObject | ConvertTo-Json -Compress
#     $uri = "http://127.0.0.1:8000/predict"
# And then run from PS below curl request
#     Invoke-RestMethod -Uri $uri -Method Post -ContentType "application/json" -Body $jsonContent

# TO RUN FAST API SERVER, RUN BELOW COMMAND ON PS PROMPT
# uvicorn app:app --reload 

# in vscode once you create project, then create virtual environment, because all libraries
# will be installed in this Environment
# Once environment is created go into this environment by executing activate script in your
# environments script folder
# Then install all required libraries in this environment
# myenv\Scripts\activate
# If uvicorn is not installed then install it in your Environment
# pip install uvicorn