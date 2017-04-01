# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
        ('kindergartens', '0002_auto_20170327_1844'),
        ('children', '0002_child_personal_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=254, verbose_name='Status', choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending')),
                ('child', models.ForeignKey(to='children.Child')),
                ('kindergarten', models.ForeignKey(to='kindergartens.Kindergarten')),
                ('parent', models.ForeignKey(to='parents.Parent')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('file', models.FileField(upload_to='attachments')),
                ('application', models.ForeignKey(to='applications.Application')),
            ],
        ),
    ]
