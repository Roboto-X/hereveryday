# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img_url',
        ),
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.FileField(default=django.utils.timezone.now, upload_to='./static/photos/test/'),
            preserve_default=False,
        ),
    ]
