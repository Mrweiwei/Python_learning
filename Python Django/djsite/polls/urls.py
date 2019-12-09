from django.urls import path#导入urls模块的path函数
from .import views1#导入views1模块
urlpatterns=[
    path('',views1.index,name='index'),   #调用index函数
]