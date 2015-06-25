# -*- coding: utf-8 -*-
__author__ = 'shenyineng'

from flask import Flask
from flask import request
from wechat_sdk import WechatBasic
from FetchResources import FetchResources
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def validate():
    signature = request.args.get('signature')
    echostr = request.args.get('echostr')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')

    token = "test"

    body_text = request.get_data()

    # 实例化 wechat
    wechat = WechatBasic(token=token)
    # 对签名进行校验
    if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        # 对 XML 数据进行解析 (必要, 否则不可执行 response_text, response_image 等操作)
        wechat.parse_data(body_text)
        # 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
        message = wechat.get_message()

        response = None

        if message.type == 'text':
            newsList = generate()
            response = wechat.response_news(newsList)

        # 现在直接将 response 变量内容直接作为 HTTP Response 响应微信服务器即可，此处为了演示返回内容，直接将响应进行输出
        return response

def generate():
    fetchResources = FetchResources()
    hot_json_result = fetchResources.fetch()

    newsList = []

    for i in range(len(hot_json_result)):
        each_post = {
            'title': u'' + hot_json_result[i]['title'] + '',
            'description': u'' + hot_json_result[i]['content'] + '',
            'picurl': u'' + hot_json_result[i]['member']['avatar_mini'] + '',
            'url': u'' + hot_json_result[i]['url'] + '',
            }

        newsList.append(each_post)

    # response = wechat.response_news([
    #     {
    #         'title': u'第一条新闻标题',
    #         'description': u'第一条新闻描述，这条新闻没有预览图',
    #         'url': u'http://www.google.com.hk/',
    #         }, {
    #         'title': u'第二条新闻标题, 这条新闻无描述',
    #         'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
    #         'url': u'http://www.github.com/',
    #         }, {
    #         'title': u'第三条新闻标题',
    #         'description': u'第三条新闻描述',
    #         'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
    #         'url': u'http://www.v2ex.com/',
    #         }
    # ])

    # print newsList
    return newsList


if __name__ == '__main__':
    # generate()
    app.run(host="0.0.0.0", port=80)