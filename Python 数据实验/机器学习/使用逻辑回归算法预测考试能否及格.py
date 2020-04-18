from sklearn.linear_model import LogisticRegression

'''根据学生某门课程的复习时长和效率预测期末是否能够及格的示例'''

#复习情况，格式为（时长，效率），其中时长单位为小时
#效率为[0,1]之间的小数，数值越大表示效率越高

X_train=[(0,0),(2,0.9),(3,0.4),(4,0.9),(5,0.4),
         (6,0.4),(6,0.8),(6,0.7),(7,0.2),(7.5,0.8),
         (7,0.9),(8,0.1),(8,0.6),(8,0.8)]
# 0表示不及格，1表示及格
y_train=[0,0,0,1,0,0,1,1,0,1,1,0,1,1]

#创建并训练逻辑回归模型
reg=LogisticRegression()
reg.fit(X_train,y_train)

#测试模型
X_test=[(3,0.9),(8,0.5),(7,0.2),(4,0.5),(4,0.7)]
y_test=[0,1,0,0,1]
score=reg.score(X_test,y_test)

#预测并输出预测结果
learning=[(5,0.9)]
#result返回的是一个二维列表:[[,]]，内容为及格和不及格的概率
result=reg.predict_proba(learning)
#print(result)
msg='''模型得分:{0}
    复习时长为：{1[0]},效率为:{1[1]}
    您不及格的概率为：{2[0]}
    您及格的概率为：{2[1]}
    综合判断，您会：{3}'''.format(score,learning[0],result[0],
                          '不及格' if result[0][0]>0.5 else '及格')
print(msg)








    
