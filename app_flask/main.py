from flask import Flask,jsonify,request,redirect
from BVWechatDB import BVWechatDB
from tool import get_access_token,get_openid
import requests
from settings import FLASK_DOMAIN_NAME,OPENID,APP_ID,APP_SECRET,TEMPLATE_ID,VUE_DOMAIN_NAME

app = Flask(__name__)

# # 发送模板消息
# def send_template_message(access_token, openid, template_id, data):
#     url = f'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}'
#     message_data = {
#         "touser": openid,
#         "template_id": template_id,
#         "data": data
#     }
#     response = requests.post(url, json=message_data)
#     return response.json()

# @app.route('/send_message', methods=['GET'])
# def send_message():
#     # 获取 access_token
#     access_token = get_access_token()
    
#     # 设置模板消息的内容（此处使用一个示例模板）
#     message_data = {
#         "first": {
#             "value": "您好，您有一条新的消息！",
#             "color": "#173177"
#         },
#         "keyword1": {
#             "value": "32元",
#             "color": "#173177"
#         },
#         "keyword2": {
#             "value": "2025-03-13",
#             "color": "#173177"
#         },
#         "remark": {
#             "value": "请注意查收。",
#             "color": "#173177"
#         }
#     }

#     # 发送模板消息
#     response = send_template_message(access_token, OPENID, TEMPLATE_ID, message_data)

#     # 返回发送结果
#     return jsonify(response)

@app.route("/wechat/bind_device")
def bind_device():
    """ 处理微信菜单点击请求，获取openid并跳转到指定URL """
    code = request.args.get("code")

    if not code:
        # 第一次请求，没有code，重定向到微信获取code
        wx_auth_url = f"https://open.weixin.qq.com/connect/oauth2/authorize?appid={APP_ID}&redirect_uri=http://yangxiao666.natapp1.cc/wechat/bind_device&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
        return redirect(wx_auth_url)

    # 通过 code 获取 openid
    token_url = f"https://api.weixin.qq.com/sns/oauth2/access_token?appid={APP_ID}&secret={APP_SECRET}&code={code}&grant_type=authorization_code"
    res = requests.get(token_url).json()

    openid = res.get("openid")
    if not openid:
        return "获取 OpenID 失败，请重试", 400

    # 跳转到目标URL并附加openid作为查询参数
    target_url = f"{VUE_DOMAIN_NAME}?openid={openid}"
    return redirect(target_url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
    