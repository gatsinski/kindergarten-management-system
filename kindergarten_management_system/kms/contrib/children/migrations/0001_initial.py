# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
        ('kindergartens', '0002_auto_20170327_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.CharField(verbose_name='First name', max_length=254)),
                ('middle_name', models.CharField(verbose_name='Middle name', max_length=254)),
                ('last_name', models.CharField(verbose_name='Last name', max_length=254)),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
                ('address', models.CharField(verbose_name='Address', max_length=254)),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('kindergarten', models.ForeignKey(to='kindergartens.Kindergarten')),
                ('parents', models.ManyToManyField(to='parents.Parent')),
            ],
            options={
                'verbose_name_plural': 'Children',
                'verbose_name': 'Child',
            },
        ),
    ]
