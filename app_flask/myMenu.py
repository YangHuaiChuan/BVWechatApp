import hashlib
import requests
from flask import Flask, request, jsonify, render_template, redirect
import urllib
import json
from settings import APP_ID,APP_SECRET,FLASK_DOMAIN_NAME

app = Flask(__name__)

@app.route("/wechat/index")
def index():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
    user_info_response = requests.get(url).json()
    access_token = user_info_response['access_token']   
    
    menu_url = f"https://api.weixin.qq.com/cgi-bin/menu/create?access_token={access_token}"

    menu_data = {
        "button": [
            {
                "name": "菜单",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "绑定设备",
                        "url": f"{DOMAIN_NAME}/wechat/bind_device"
                    }
                ]
            }
        ]
    }

    response = requests.post(menu_url, data=json.dumps(menu_data, ensure_ascii=False).encode('utf-8'),
                             headers={'Content-Type': 'application/json; charset=UTF-8'})

    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)