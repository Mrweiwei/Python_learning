from django.shortcuts import render
from django.http import HttpResponse #为访问的URL用户返回指定内容，在浏览器显示
def index(request):
    return HttpResponse("Hello,world.You're at the polls index")#返回内容
