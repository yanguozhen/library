# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='readerName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='manager',
            old_name='rpwd',
            new_name='pwd',
        ),
    ]
