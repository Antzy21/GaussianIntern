# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sankey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
    ]
