#read()方法是读取文件中指定数量的字符而不是字节，对中文和英文字母同等对待

f=open('sample.txt','r')
while True:
    line=f.readline()
    if line=='':
        break
    print(line,end='')
f.close()

#readlines()不建议使用太占内存了
