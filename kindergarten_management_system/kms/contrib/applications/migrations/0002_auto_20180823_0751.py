# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('test', models.CharField(verbose_name='Test', max_length=254)),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TestTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(verbose_name='Language', max_length=15, db_index=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('master', models.ForeignKey(null=True, editable=False, related_name='translations', to='applications.Test')),
            ],
            options={
                'verbose_name': 'test Translation',
                'db_table': 'applications_test_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='testtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
