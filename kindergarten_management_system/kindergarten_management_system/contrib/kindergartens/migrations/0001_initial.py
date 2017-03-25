# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=254)),
            ],
            options={
                'verbose_name': 'Kindergarten',
                'verbose_name_plural': 'Kindergartens',
            },
        ),
        migrations.CreateModel(
            name='Kindergarten',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=254)),
                ('address', models.CharField(verbose_name='Address', max_length=254)),
                ('city', models.ForeignKey(to='kindergartens.City')),
            ],
            options={
                'verbose_name': 'Kindergarten',
                'verbose_name_plural': 'Kindergartens',
            },
        ),
        migrations.CreateModel(
            name='KindergartenType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=254)),
            ],
            options={
                'verbose_name': 'Kindergarten',
                'verbose_name_plural': 'Kindergartens',
            },
        ),
        migrations.AddField(
            model_name='kindergarten',
            name='type',
            field=models.ForeignKey(to='kindergartens.KindergartenType'),
        ),
    ]
