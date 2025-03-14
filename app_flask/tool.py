import requests
from settings import APP_ID,APP_SECRET
from flask import Flask,request,redirect

app = Flask(__name__)

def get_access_token():
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}'
    response = requests.get(url)
    data = response.json()
    return data['access_token']

@app.route("/wechat/getopenid")
def get_openid():
    code = request.args.get("code")

    if not code:
        # 第一次请求，没有code，重定向到微信获取code
        wx_auth_url = f"https://open.weixin.qq.com/connect/oauth2/authorize?appid={APP_ID}&redirect_uri=http://yangxiao666.natapp1.cc/wechat/getopenid&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
        return redirect(wx_auth_url)

    # 通过 code 获取 openid
    print("获取code")
    token_url = f"https://api.weixin.qq.com/sns/oauth2/access_token?appid={APP_ID}&secret={APP_SECRET}&code={code}&grant_type=authorization_code"
    res = requests.get(token_url).json()

    openid = res.get("openid")
    print(openid)

    if not openid:
        return "获取 OpenID 失败，请重试", 400

    return openid
