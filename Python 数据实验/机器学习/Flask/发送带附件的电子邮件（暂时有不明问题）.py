import os.path
from flask import Flask
from flask_mail import Mail,Message


app=Flask(__name__)

#以163免费的邮箱为例
app.config['MAIL_SERVER']='smtp.163.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=True

#如果电子邮件地址是abcd@163.com,那么应填写abcd
app.config['MAIL_USERNAME']='weiweiweijie163@163.com'
app.config['MAIL_PASSWORD']='BEZQJXMCTQIGIJJI'

def sendEmail(From,To,Subject,Body,Html,Attachments):
    '''To:must be a list'''
    msg=Message(Subject,sender=From,recipients=To)
    msg.body=Body
    msg.html=Html
    for f in Attachments:
        with app.open_resource(f) as fp:
            msg.attach(filename=os.path.basename(f),data=fp.read(),content_type=\
                       'application/octet-stream')
        mail=Mail(app)
        with app.app_context():
            mail.send(msg)

if __name__=='__main__':
    #From填写的电子邮箱地址必须与前面配置的相同
    From='<Mrweiwei_peter>'
    #作者的QQ邮箱
    To=['<827045489@qq.com>']
    Subject='hello world!'
    Body='only a test.'
    Html='<h1>test test test</h1>'
    Attachments=['helloworld.py']
    sendEmail(From,To,Subject,Body,Html,Attachments)




























