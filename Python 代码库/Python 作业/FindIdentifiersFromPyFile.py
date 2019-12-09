#编写程序，提取Python程序中的类名、函数名以及变量名等标识符(在命令提示符环境中使用命令Python FindIndentifiersFromPyFile.py)

import re
import os
import sys

classes={}
functions=[]
variables={'normal':{},'parametter':{},'infor':{}}
'''This is a test string:
atest,btest=3,5
to verify that variables in comments will be ignored by this algorithm'''

def _identifyClassNames(index,line):
    '''parametter index is the line number of line,
parameter line is a line of code of the file to check'''
    pattern=re.compile(r'(?<=class\s)\w+(?=.*?:)$')
    matchResult=pattern.search(line)
    if not matchResult:
        return
    className=matchResult.group(0)
    classes[className]=classes.get(classes,[])
    classes[className].append(index)

def _identifyFunctionName(index,line):
    pattern=re.compile(r'(?<=def\s)(\w+)\((.*?)\)(?=:)$')
    matchResult=pattern.search(line)
    if not matchResult:
        return
    functionName=matchResult.group(1)
    functions.append((functionName,index))
    parameters=matchResult.group(2).split(r',')
    if parameters[0]=='':
        return
    for v in parameter:
        variables['parameter'][v]=variables['parameter'].get(v,[])
        variables['parameter'][v].append(index)

def _identifyVariableNames(index,line):
    #find normal variables,including the case:a,b=3,5
    pattern=re.compile(r'\b(.*?)(?=\s=)$')
    matchResult=pattern.search(line)
    if matchResult:
        vs=matchResult.group(1).split(r',')
        for v in vs:
            #consider the case 'if variable==value'
            if 'if' in v:
                v=v.split()[1]
            #consider the case:'a[3]=3'
            if '[' in v:
                v=v[0:v.index('[')]
            variables['normal'][v]=variables['normal'].get(v,[])
            variables['normal'][v].append(index)
        #find the variables in for statements
        pattern=re.compile(r'(?<=for\s)(.*?)(?=\sin)$')
        matchResult=pattern.search(line)
        if matchResult:
            vs=matchResult.group(1).split(r',')
            for v in vs:
                variables['infor'][v]=variables['infor'].get(v,[])
                variables['infor'][v].append(index)

def output():
    print('='*30)
    print('The class names and their line numbers are:')
    for key,value in classes.items():
        print(key,':',value)
    print('='*30)
    print('The function names and their line number are:')
    for i in functions:
        print(i[0],':',i[1])
    print('='*30)
    print('The normal variable names and their line numbers are:')
    for key,value in variable['normal'].items():
        print(key,':',value)
    print('-'*20)
    print('The parameter names and their line numbers are:')
    for key,value in variables['parameter'].items():
        print(key,':',value)
    print('-'*20)
    print('The variable names and their line numbers in for statements are:')
    for key,value in variables['infor'].items():
        print(key,':',value)

#suppose the lines of comments less than 50
def comments(index):
    for i in range(50):
        line=aIIlines[index+i].strip()
        if line.endswith('"""')or line.endswith("'''"):
            return i+1


if __name__=='__main__':
    fileName=sys.argv[1]
    if not os.path.isfile(fileName):
        print('Your input is not a file.')
        sys.exit(0)

    aIIlines=[]
    with open(fileName,'r')as fp:
        aIIlines=fp.readlines()
    index=0
    totalLen=len(aIIlines)
    while index<totalLen:
        line=aIIlines[index]
        #strip the blank characters at both end of line
        line=line.strip()
        #ignore the comments starting with '#'
        if line.startswith('#'):
            index+=1
            continue
        #ignore the comments between ''' or """
        if line.startswith('"""') or line.startswith("'''"):
            index+=comments(index)
            continue
        #identify.identifiers
        _identifyClassNames(index+1,line)
        _identifyFunctionNames(index+1,line)
        _identifyVariableNames(index+1,line)
        index+=1
    output()

























    
























    





















        

















































