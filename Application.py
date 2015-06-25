__author__ = 'shenyineng'

from flask import Flask
from flask import request
from xml.dom import minidom

app = Flask(__name__)

@app.route('/', methods=['GET'])
def validate():
    signature = request.args.get('signature')
    echostr = request.args.get('echostr')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')

    print(signature)
    print(echostr)
    print(timestamp)
    print(nonce)

    return echostr

@app.route('/', methods=['POST'])
def handler():
    data = request.get_data()
    doc = minidom.parseString(data)
    print doc.getElementsByTagName("FromUserName")

    # print(request.get_data())



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)