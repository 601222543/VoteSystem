# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objName', models.CharField(max_length=32, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('objCreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u9879\u76ee\u540d\u79f0',
                'verbose_name_plural': '\u9879\u76ee\u540d\u79f0',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=32, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9')),
                ('polls', models.IntegerField(default=0, verbose_name=b'\xe7\xa5\xa8\xe6\x95\xb0')),
                ('optionCreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('obj', models.ForeignKey(to='vote.Obj')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u9009\u9879',
                'verbose_name_plural': '\u9009\u9879',
            },
        ),
    ]
