# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 12:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first1', '0003_auto_20170711_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pie1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MaxValueValidator(limit_value=100)])),
            ],
        ),
    ]
