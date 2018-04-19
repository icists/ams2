# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-19 01:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180418_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='assigned_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='policy.Room'),
        ),
    ]
