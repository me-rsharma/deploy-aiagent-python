from fastapi import FastAPI
import os

app = FastAPI()

PORT = os.environ.get('PORT', 9999)
MY_PROJECT = os.environ.get('MY_PROJECT', 'My Project Name')
#MY_PROJECT = os.environ.get('MY_PROJECT') or 'My Project Name' # this will also a valid syntax
API_KEY = os.environ.get('API_KEY')

@app.get("/")
def read_index():
    return {"greet": "hari bol", "project_name": MY_PROJECT, 'api_key': API_KEY}