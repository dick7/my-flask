# -*- coding: UTF-8 -*-

import time
import hashlib
from lxml import etree
from flask import request
from flask import Flask, make_response    # 这些是本例中所有用到的库

# 编写服务端程序
class Message(object):
    def __init__(self, req):
        self.request = req
        self.token = '【这里填刚刚公众号页面上的项目】'
        self.AppID = '【这里填刚刚公众号页面上的项目】'
        self.AppSecret = '【这里填刚刚公众号页面上的项目】'


class Get(Message):
    def __init__(self, req):
        super(Get, self).__init__(req)
        self.signature = req.args.get('signature')    # 这里分别获取传入的四个参数
        self.timestamp = req.args.get('timestamp')
        self.nonce = req.args.get('nonce')
        self.echostr = req.args.get('echostr')
        self.return_code = 'Invalid'

    def verify(self):
        data = sorted([self.token, self.timestamp, self.nonce])    # 字典排序
        string = ''.join(data).encode('utf-8')    # 拼接成字符串
        hashcode = hashlib.sha1(string).hexdigest()    # sha1加密
        if self.signature == hashcode:
            self.return_code = self.echostr


# 接收用户消息，[微信公众平台](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/wiki%3Ft%3Dresource/res_main)
class Post(Message):
    def __init__(self, req):
        super(Post, self).__init__(req)
        self.xml = etree.fromstring(req.stream.read())
        self.MsgType = self.xml.find("MsgType").text
        self.ToUserName = self.xml.find("ToUserName").text
        self.FromUserName = self.xml.find("FromUserName").text
        self.CreateTime = self.xml.find("CreateTime").text
        self.MsgId = self.xml.find("MsgId").text

        hash_table = {
            'text': ['Content'],
            'image': ['PicUrl', 'MediaId'],
            'voice': ['MediaId', 'Format'],
            'video': ['MediaId', 'ThumbMediaId'],
            'shortvideo': ['MediaId', 'ThumbMediaId'],
            'location': ['Location_X', 'Location_Y', 'Scale', 'Label'],
            'link': ['Title', 'Description', 'Url'],
        }
        attributes = hash_table[self.MsgType]
        self.Content = self.xml.find("Content").text if 'Content' in attributes else '抱歉，暂未支持此消息。'
        self.PicUrl = self.xml.find("PicUrl").text if 'PicUrl' in attributes else '抱歉，暂未支持此消息。'
        self.MediaId = self.xml.find("MediaId").text if 'MediaId' in attributes else '抱歉，暂未支持此消息。'
        self.Format = self.xml.find("Format").text if 'Format' in attributes else '抱歉，暂未支持此消息。'
        self.ThumbMediaId = self.xml.find("ThumbMediaId").text if 'ThumbMediaId' in attributes else '抱歉，暂未支持此消息。'
        self.Location_X = self.xml.find("Location_X").text if 'Location_X' in attributes else '抱歉，暂未支持此消息。'
        self.Location_Y = self.xml.find("Location_Y").text if 'Location_Y' in attributes else '抱歉，暂未支持此消息。'
        self.Scale = self.xml.find("Scale").text if 'Scale' in attributes else '抱歉，暂未支持此消息。'
        self.Label = self.xml.find("Label").text if 'Label' in attributes else '抱歉，暂未支持此消息。'
        self.Title = self.xml.find("Title").text if 'Title' in attributes else '抱歉，暂未支持此消息。'
        self.Description = self.xml.find("Description").text if 'Description' in attributes else '抱歉，暂未支持此消息。'
        self.Url = self.xml.find("Url").text if 'Url' in attributes else '抱歉，暂未支持此消息。'
        self.Recognition = self.xml.find("Recognition").text if 'Recognition' in attributes else '抱歉，暂未支持此消息。'


# 回复用户消息
class Reply(Post):
    def __init__(self, req):
        super(Reply, self).__init__(req)
        self.xml = f'<xml><ToUserName><![CDATA[{self.FromUserName}]]></ToUserName>' \
                   f'<FromUserName><![CDATA[{self.ToUserName}]]></FromUserName>' \
                   f'<CreateTime>{str(int(time.time()))}</CreateTime>'

    def text(self, Content):
        self.xml += f'<MsgType><![CDATA[text]]></MsgType>' \
                    f'<Content><![CDATA[{Content}]]></Content></xml>'

    def image(self, MediaId):
        pass

    def voice(self, MediaId):
        pass

    def video(self, MediaId, Title, Description):
        pass

    def music(self, ThumbMediaId, Title='', Description='', MusicURL='', HQMusicUrl=''):
        pass
        
    def reply(self):
        response = make_response(self.xml)
        response.content_type = 'application/xml'
        return response


# 验证消息
app = Flask(__name__)

@app.route("/wx", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        message = Get(request)
        message.verify()
        return message.return_code

    elif request.method == "POST":
        message = Reply(request)
        message.text(message.Content)
        return message.reply()


if __name__ == "__main__":
    # app.run(port=5050)
    app.run()

