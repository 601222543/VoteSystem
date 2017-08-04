# coding: utf-8
from django.contrib import admin
from models import *

class ObjTempAdmin(admin.TabularInline):
    model = Option # 将models中的Option类放到这里
    extra = 3 # 设置默认的添加数量为3个

class ObjAdmin(admin.ModelAdmin):
    inlines = [ObjTempAdmin] # 将上面链接有Obj的中间过渡类，放到这里，这样后台就完成了两个表的外键链接
    list_display = ['id', 'objName', 'objCreateTime', 'flog']
    list_filter = ["objCreateTime"]

class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'option', 'polls', 'optionCreateTime']
    list_filter = ["optionCreateTime"]

admin.site.register(Obj, ObjAdmin)
admin.site.register(Option, OptionAdmin)


