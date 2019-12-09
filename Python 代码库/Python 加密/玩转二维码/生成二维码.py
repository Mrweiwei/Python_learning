#生成二维码
'''Python扩展库qrcode提供了生成二维码的功能，可以使用户pip工具安装，生成的二维码可以用手机微信扫描并识别其中的信息'''

import qrcode

qr=qrcode.QRCode(version=10,box_size=10,border=4,error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('www.baidu.com')
qr.make(fit=True)
img=qr.make_image()
img.save('Python_baidu.png')
