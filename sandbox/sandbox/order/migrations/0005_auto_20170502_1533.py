# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20160111_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='guest_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Guest email address'),
        ),
    ]