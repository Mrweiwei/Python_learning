from aip import AipNlp

APP_ID='19122578'
API_KEY='e8d071gY19ns8XyOxh5GrSry'
SECRET_KEY='LXmHT90WXhiGvexhsGd9FLabt6PSGtDf'

client=AipNlp(APP_ID,API_KEY,SECRET_KEY)

#text='真希望快点开学'

#print(client.dnnlm(text)["items"])

email=[{'title':'你好啊'},
       {'title':'这是垃圾邮件'},
       {'title':'你是狗'},
       {'title':'你是猪'}
       ]
stop_word={}.fromkeys(['狗','虫子','猫','猪'])

def classify(lst,j):
    for word in lst:
    #print(word)
        if word not in stop_word:
            email[j]["category_id"]=0
        else:
            email[j]["category_id"]=1
        
    '''if flag ==True:
        print("分类的得出的结果为垃圾邮件!")
        email[j]["category_id"]=1
    else:
        print("这是正常的邮件!")
        email[j]["category_id"]=0'''


for j in range(len(email)):
    text=email[j]["title"]
    lst=client.dnnlm(text)['items']
    done=[]
    for i in range(len(lst)):
        done.append(str(lst[i]['word']))
        if '，' in done:
            done.remove('，')
    #print(done)
    classify(done,j)

        
print(email)
