# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='item_stock',
            field=models.IntegerField(default=0),
        ),
    ]
