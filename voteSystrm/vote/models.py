# coding: utf-8
from django.db import models

class Obj(models.Model):
    objName = models.CharField(max_length=32, blank=False, verbose_name="项目名称")
    objCreateTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    flog = models.IntegerField(default=0) #0为单选，1为多选

    def __unicode__(self):
        return self.objName

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"
        ordering = ["id"]

class Option(models.Model):
    obj = models.ForeignKey(Obj) # 创建外键
    option = models.CharField(max_length=32, blank=False, verbose_name="选项")
    polls = models.IntegerField(default=0, verbose_name="票数")
    optionCreateTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.option

    class Meta:
        verbose_name = "选项"
        verbose_name_plural = "选项"
        ordering = ["id"]


