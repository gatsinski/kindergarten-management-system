# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBlockPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, to='cms.CMSPlugin', primary_key=True, related_name='cms_content_blocks_contentblockpluginmodel', parent_link=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=254)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=254)),
                ('type', models.CharField(choices=[('cadet_blue', 'Cadet blue'), ('burlywood', 'Burlywood'), ('azure', 'Azure'), ('alice_blue', 'Alize blue'), ('corn_silk', 'Corn silk')], default='cadet_blue', verbose_name='Block type', max_length=254)),
            ],
            options={
                'verbose_name': 'Content blok',
                'verbose_name_plural': 'Content blocks',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
