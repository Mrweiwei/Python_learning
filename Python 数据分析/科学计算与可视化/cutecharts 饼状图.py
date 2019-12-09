#饼状图

from cutecharts.charts import Pie

def pie_base()->Pie:
    chart=Pie("一年内商品消费饼状图")
    chart.set_options(['商品','衣服','电器','书籍','化妆品'])
    chart.add_series([30000,15000,8000,2000,10000])
    return chart

pie_base().render("图表/一年内商品消费饼状图.html")
