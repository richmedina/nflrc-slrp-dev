# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-24 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lltsite', '0011_remove_impactfactor_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impactfactor',
            old_name='factor',
            new_name='current_factor',
        ),
    ]
