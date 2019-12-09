#利用pandas库对大量数据处理成二维数据结构
import pandas as pd

excelFile=r'Mysql数据库中导出的数据.xlsx'
df=pd.DataFrame(pd.read_excel(excelFile))
df1=df[["商品名称","数量","金额"]]
print(df1)

'''read_excel函数的各参数：
def read_excel(io, sheet_name=0, header=0, skiprows=None, skip_footer=0,
               index_col=None, names=None, usecols=None, parse_dates=False,
               date_parser=None, na_values=None, thousands=None,
               convert_float=True, converters=None, dtype=None,
               true_values=None, false_values=None, engine=None,
                squeeze=False, **kwds):             
'''
