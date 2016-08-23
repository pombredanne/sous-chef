# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0005_fix241b'),
        ('member', '0013_client_ingredients_to_avoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='components_to_avoid',
            field=models.ManyToManyField(through='member.Client_avoid_component', to='meal.Component'),
        ),
    ]
