# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_books_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='updated',
        ),
    ]
