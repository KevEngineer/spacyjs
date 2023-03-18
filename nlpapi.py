import spacyextractor
#import python flask to create a rest API
from flask import Flask
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/search/{query}')
def hello_world(query):
   pageResult=spacyextractor.extractEntities(query)
   return pageResult
