from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt


background_Image=plt.imread('love.jpg')
wc=WordCloud(background_color='black',
             scale=32,
             margin=1,
             mask=background_Image,
             font_path='C:\WINDOWS\Fonts\simhei.ttf',
             max_font_size=100,
             random_state=30
             )

text=open(r'詹姆斯.txt',encoding='utf-8').read()
wc.generate(text)
img_colors=ImageColorGenerator(background_Image)
wc.recolor(color_func=img_colors)
wc.to_file('new.jpg')
