# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_books_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='Author',
            field=models.CharField(default='Ayushman', max_length=50),
        ),
    ]
