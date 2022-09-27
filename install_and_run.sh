#!/bin/bash

# To install on start of server
#sudo apt update
#sudo apt -y install git
#sudo apt -y install python3-pip
pip3 install "fastapi[all]"
#sudo apt -y install uvicorn
#cd /home/ubuntu/
#git clone https://github.com/Danielcourvoisier/cloudsys-lab1-server.git
#export S3_BUCKET_ADR=https://sos-ch-dk-2.exo.io/cloudsys-lab1/test.json

# Run Client
cd /home/ubuntu/cloudsys-lab1-server/
uvicorn main:app --host 0.0.0.0 --port 8080