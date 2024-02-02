from fastapi import FastAPI
import numpy as np 

app = FastAPI()

@app.get("/")
def read_root():
    return {"LFC"}