# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0005_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_group_size', models.PositiveSmallIntegerField(verbose_name='minimum group size')),
            ],
            options={
                'verbose_name': 'other configuration',
            },
        ),
        migrations.CreateModel(
            name='EssayTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='stage',
            name='current_stage',
            field=models.CharField(choices=[('BE', 'Before Early'), ('E', 'Early'), ('EC', 'Early Closed'), ('R', 'Regular'), ('RC', 'Regular Closed'), ('L', 'Late'), ('LC', 'Late Closed')], max_length=2),
        ),
    ]
