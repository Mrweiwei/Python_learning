#可视化库cutecharts基本使用

'''目前cutecharts支持的可视化图像类型有：柱状图、折线图、饼状图、雷达图、散点图。
后续会添加比如：词云图、3D柱状图、条形图等等'''

#导入cutecharts中的Bar
from cutecharts.charts import Bar
#导入测试用例
#from cutecharts.faker import Faker

def bar_base()->Bar:
    chart=Bar("一月份的商品消费情况")
    chart.set_options(labels=['食品','衣服','电器','书籍','化妆品'],x_label="消费类别（类）",y_label="消费金额（元）")
    chart.add_series("消费品",[1500,2000,3000,500,1000])
    return chart

bar_base().render("图表/一月份的商品消费情况柱状图.html")

'''.render("html_name.html"):生成一个本地文件，html_name为文件名(html文件),默认名
为:render.html
   .render_notebook():可以在jupyter中直接运行显示。
'''
