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
#bucket_url = "https://sos-ch-gva-2.exo.io/cloudsys-lab1-bucket/test.json"
#app_port = 8000


# Get host ip_adress
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


# Get json file from object storage
def get_s3_file():
    response_API = requests.get(bucket_url)
    data = response_API.text
    data = json.loads(data)
    return data


app = FastAPI()


# root
@app.get("/", response_class=HTMLResponse)
async def root():
    #return FileResponse('index.html')
    return """
    <html>
        <head>
            <title>CloudSys Lab1</title>
        </head>
        <body>
            <h1>Hey, you are on my server!</h1>
            <p>
            window.location.href
            My IP Address is: {ip}
            <p>
            This server get data from: 
            <a href="{bucket_url}">{bucket_url}</a>
            <p>
            And you can get this data here:
            <a id="data_link" href=""> Get the data </a>
            <p>
            <script>
                data_url = window.location.href + "data";
                document.getElementById("data_link").href = data_url;
            </script>
        </body>
    </html>
    """.format(ip=get_ip_address(), bucket_url=bucket_url, port=app_port)


# Get json file/data stored on s3/bucket
@app.get("/data")
async def data():
    data = get_s3_file()
    print(data)
    return data