# coding: utf-8
from django.shortcuts import render
from models import Obj, Option

def index(request):
    objs = Obj.objects.all()
    context = {'objs': objs}
    return render(request, 'index.html', context)

def show(request, id):
    obj = Obj.objects.get(pk=id) # 获取主表的数据
    optionTable = obj.option_set # 获取子表的表
    optionContent = optionTable.all() # 获取子表的对象
    context = {'obj':obj, 'optionContent':optionContent}
    return render(request, 'show.html', context)

def showAction(request, id):
    obj = Obj.objects.get(pk=id)  # 获取主表的数据
    optionTable = obj.option_set  # 获取子表的表
    optionContent = optionTable.all()
    if obj.flog:
        choiceId = request.POST.getlist('myOption') #获取用户所投选项的id
        if choiceId == []:
            context = {'obj': obj, 'optionContent': optionContent,'getError': "你倒是选一个呀SB！"}
            return render(request, 'show.html', context)
        for idNum in choiceId:
            optionObj = optionTable.get(pk=idNum) # 提取用户所投选项的对象文件
            optionObj.polls += 1 # 将用户所投选项的票数增加1
            optionObj.save() # 保存该对象的更改
    else:
        try:
            choiceId = request.POST['myOption'] #获取用户所投选项的id
        except KeyError,Option.DoesNotExist:
            context = {'obj': obj, 'optionContent': optionContent,'getError': "你倒是选一个呀SB！"}
            return render(request, 'show.html', context)
        optionObj = optionTable.get(pk=choiceId) # 提取用户所投选项的对象文件
        optionObj.polls += 1 # 将用户所投选项的票数增加1
        optionObj.save() # 保存该对象的更改

    # 将保存后的数据渲染到页面
    obj = Obj.objects.get(pk=id)
    optionTable = obj.option_set
    optionContent = optionTable.all()
    context = {'obj': obj, 'optionContent': optionContent}
    return render(request, 'showResult.html', context)


