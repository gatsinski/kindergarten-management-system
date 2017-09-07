# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindergartens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=254)),
                ('description', models.CharField(verbose_name='Description', max_length=1000)),
                ('kindergarten', models.ForeignKey(to='kindergartens.Kindergarten')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='GroupType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=254)),
            ],
            options={
                'verbose_name': 'Group type',
                'verbose_name_plural': 'Group types',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='type',
            field=models.ForeignKey(to='kindergartens.GroupType'),
        ),
    ]
