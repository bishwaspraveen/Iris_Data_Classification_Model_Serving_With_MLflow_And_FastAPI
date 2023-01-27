from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
from io import StringIO
import requests

app = FastAPI()

#Created so that this could be used as a blueprint to sent these parameters in the request body
class IrisSpecies(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

#Default end point / root end point
@app.get("/")
async def root():
    return {"message" : "Hello Bishwas! This is the entry point for your application"}

#Prediction endpoint to classfiy a single test sample into its specific class
@app.post('/predict')
async def predict_species(iris:IrisSpecies):
    data = iris.dict()
    data_in = [[data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]]
    print (data_in)
    #The server end point which is generated by MLflow server to predict outputs
    end_point = "http://localhost:1234/invocations"
    inference_request = {
        "data" : data_in
    }
    print (inference_request)
    response = requests.post(end_point, json=inference_request)
    print (response)
    return {
        'prediction' : response.text
    }

@app.post('/files')
async def predict_file(file: bytes = File(...)):
    s = str(file, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    lst = df.values.tolist()
    inference_request = {
        "data" : lst
    }
    end_point = "http://localhost:1234/invocations"
    print (inference_request)
    response = requests.post(end_point, json=inference_request)
    print (response.text)
    return response.text