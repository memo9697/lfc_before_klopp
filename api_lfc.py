from fastapi import FastAPI
import numpy as np
from train_model import make_model_save
from make_pred import make_prediction

app = FastAPI()

@app.get("/infos")
def read_root():
    return {"LFC"}

@app.get("/train_model")
def train_model():
    make_model_save()
    print('Training in progress')
    return {"Response": "Training completed."}

@app.get("/{x1}/{x2}")
def get_pred(x1: float, x2: int):
    p1 = [x1,x2]
    x = np.array([p1])
    print('x', x)
    
    prediction = make_prediction(x)

    print(prediction)

    return {"prediction": prediction}