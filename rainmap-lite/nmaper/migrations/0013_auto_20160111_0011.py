# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmaper', '0012_auto_20160109_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nmapscan',
            name='uuid',
            field=models.CharField(max_length=32),
        ),
    ]
