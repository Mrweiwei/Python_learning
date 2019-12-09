#制作允儿动态图
'''myql库不支持中文!'''
from MyQR import myqr
import os

version,level,qr_name=myqr.run(
    # 可以是字符串，也可以是网址(前面要加http(s)://)
    words="https://v.qq.com/x/page/j3011q2qv32.html",
    # 设置容错率为最高
    version=1,
    # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    level='H',
    # 将二维码和图片合成
    picture="yuner.gif",
    # 彩色二维码
    colorized=True,
    #用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
    contrast=1.0,
    #用来调节图片的亮度，其余用法和取值同上
    brightness=1.0,
    # 保存文件的名字，格式可以是jpg,png,bmp,gi
    save_name="beautiful.gif",
    #控制位置
    save_dir=os.getcwd()
    )
