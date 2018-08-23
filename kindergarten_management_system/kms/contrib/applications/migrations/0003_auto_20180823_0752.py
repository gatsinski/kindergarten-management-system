# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20180823_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestInline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('test', models.ForeignKey(to='applications.Test')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TestInlineTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(verbose_name='Language', max_length=15, db_index=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('master', models.ForeignKey(null=True, editable=False, related_name='translations', to='applications.TestInline')),
            ],
            options={
                'verbose_name': 'test inline Translation',
                'db_table': 'applications_testinline_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='testinlinetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
