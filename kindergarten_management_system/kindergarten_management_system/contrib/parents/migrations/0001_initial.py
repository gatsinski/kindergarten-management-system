# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('middle_name', models.CharField(verbose_name='Middle name', max_length=254)),
                ('address', models.CharField(verbose_name='Address', max_length=254)),
                ('telephone', models.CharField(verbose_name='Phone', max_length=15)),
            ],
            options={
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Parents',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
