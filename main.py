import os
import requests
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse
import socket

# Get bucket name from env variable
bucket_url = os.environ["BUCKET_URL"]
app_port = os.environ["APP_PORT"]


# Get the json file from object storage (bucket)
def get_s3_file():
    response_API = requests.get(bucket_url)
    data = response_API.text
    data = json.loads(data)
    return data


app = FastAPI()


# root
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>CloudSys Lab1</title>
        </head>
        <body>
            <h1>Hey, you are on my server!</h1>
            <p>
            My address: <a id="server_url" href=""> </a>
            <p>
            This server get data from: 
            <a href="{bucket_url}">{bucket_url}</a>
            <p>
            And you can get this data here:
            <a id="data_link" href=""> Get the data </a>
            <p>
            <script>
                url = window.location.href;
                data_url = url + "data";
                document.getElementById("server_url").innerHTML = url;
                document.getElementById("server_url").href = url
                document.getElementById("data_link").href = data_url;
            </script>
        </body>
    </html>
    """.format(bucket_url=bucket_url)


# Get json file/data stored on s3/bucket
@app.get("/data")
async def data():
    data = get_s3_file()
    print(data)
    return data