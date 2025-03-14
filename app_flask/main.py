from flask import Flask,jsonify,request,redirect
from BVWechatDB import BVWechatDB
from tool import get_access_token
import requests
import json
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

@app.route("/wechat/to_bind_device")
def to_bind_device():
    """ 处理微信菜单点击请求，获取openid并跳转到指定URL """
    code = request.args.get("code")

    if not code:
        # 第一次请求，没有code，重定向到微信获取code
        wx_auth_url = f"https://open.weixin.qq.com/connect/oauth2/authorize?appid={APP_ID}&redirect_uri=http://yangxiao666.natapp1.cc/wechat/to_bind_device&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
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

@app.route('/wechat/bind_device', methods=['POST'])
def bind_device():
    # print("调用绑定设备接口")
    device_id = request.args.get("deviceId")
    password = request.args.get("password")
    openid = request.args.get("openid")
    
    print(device_id)
    print(password)
    print(openid)

    if not device_id or not password or not openid:
        return jsonify({"code": 401, "message": "后端未接收到想要的数据", "data": {}})

    # 处理逻辑，例如数据库查询或设备绑定操作
    db = BVWechatDB()
    if (db.device_is_exist(device_id) == False):
        return jsonify({"code": 402, "message": "设备ID不存在", "data": {}})

    if(db.deviceId_password_right(device_id,password) == False):
        return jsonify({"code": 403, "message": "设备密码错误", "data": {}})

    # 将openid和设备id绑定，插入数据库
    if(db.bind_device_openid(device_id,openid) == False):
        return jsonify({"code": 405, "message": "设备绑定失败", "data": {}})
    
    # print("返回数据")
    return jsonify({"code": 200, "message": "设备绑定成功", "data": {}})
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    