# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='personal_id',
            field=models.BigIntegerField(default=0, verbose_name='Personal ID'),
            preserve_default=False,
        ),
    ]
