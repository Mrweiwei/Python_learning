#散点图

from cutecharts.charts import Scatter
#from cutecharts.faker import Faker

def scatter_base()->Scatter:
    chart=Scatter("一年内商品消费情况散点图")
    chart.set_options(x_label="月份（月）",y_label="金额（元）",x_tick_count=12,y_tick_count=12)
    chart.add_series(
        "食品",[(z[0],z[1]) for z in zip([1,2,3,4,5,6,7,8,9,10,11,12],[1500,2000,3000,2500,2000,1200,2600,3100,4800,2100,4500,3300])]
        )
    chart.add_series(
        "衣服",[(z[0],z[1]) for z in zip([1,2,3,4,5,6,7,8,9,10,11,12],[2000,1000,3200,2340,2540,1210,1200,1100,1800,2100,2500,3100])]
        )
    chart.add_series(
        "电器",[(z[0],z[1]) for z in zip([1,2,3,4,5,6,7,8,9,10,11,12],[3000,2500,2900,2503,2300,1270,2690,2100,2400,2190,2500,2900])]
        )
    chart.add_series(
        "书籍",[(z[0],z[1]) for z in zip([1,2,3,4,5,6,7,8,9,10,11,12],[500,200,300,250,200,120,260,310,480,210,450,330])]
        )
    chart.add_series(
        "化妆品",[(z[0],z[1]) for z in zip([1,2,3,4,5,6,7,8,9,10,11,12],[1000,2020,3030,2520,2020,1220,2620,3120,4820,2120,4520,3120])]
        )
    return chart

scatter_base().render("图表/一年内商品消费情况散点图.html")
