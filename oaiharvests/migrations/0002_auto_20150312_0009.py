# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oaiharvests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataelement',
            name='record',
            field=models.ForeignKey(related_name='data', to='oaiharvests.Record', null=True),
            preserve_default=True,
        ),
    ]
