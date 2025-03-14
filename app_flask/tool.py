import requests
from settings import APP_ID,APP_SECRET
from flask import Flask,request,redirect

app = Flask(__name__)

def get_access_token():
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}'
    response = requests.get(url)
    data = response.json()
    return data['access_token']
