import os
import requests
import json
from fastapi import FastAPI

# Get bucket name from env variable
bucket_adr = os.environ["S3_BUCKET_ADR"]

# Get json file from object storage
def get_s3_file():
    response_API = requests.get(bucket_adr)
    data = response_API.text
    data = json.loads(data)
    return data


app = FastAPI()

@app.get("/")
async def root():
    data = get_s3_file()
    print(data)
    return data


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
