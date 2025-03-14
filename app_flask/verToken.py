from flask import Flask, request
import hashlib
from settings import TOKEN

app = Flask(__name__)

@app.route("/wechat", methods=["GET"])
def wechat_verify():
    """验证微信服务器 Token"""
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    if not all([signature, timestamp, nonce, echostr]):
        return "Missing parameters"

    # 1. 排序
    data = [TOKEN, timestamp, nonce]
    data.sort()

    # 2. 拼接字符串并进行 SHA1 加密
    hashcode = hashlib.sha1("".join(data).encode("utf-8")).hexdigest()

    # 3. 验证签名
    if hashcode == signature:
        return echostr  # 认证成功，返回微信要求的 `echostr`
    else:
        return "Verification failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
