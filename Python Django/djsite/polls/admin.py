from django.contrib import admin
from .models import Question,Choice
admin.site.register(Question)
admin.site.register(Choice)#在后台里注册投票功能对象
# Register your models here.
