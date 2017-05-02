# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_calc', '0004_auto_20170417_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='cost',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='dish',
            name='lipidsNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dish',
            name='proteinsNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=100),
        ),
    ]
