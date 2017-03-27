# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('kindergartens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Specialty',
                'verbose_name_plural': 'Specialties',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True, auto_created=True)),
                ('middle_name', models.CharField(max_length=254, verbose_name='Middle name')),
                ('address', models.CharField(max_length=254, verbose_name='Address')),
                ('telephone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('kindergarten', models.ForeignKey(to='kindergartens.Kindergarten')),
                ('specialty', models.ForeignKey(to='teachers.Specialty')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
