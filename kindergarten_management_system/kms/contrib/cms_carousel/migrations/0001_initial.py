# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselContainerPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cms_carousel_carouselcontainerpluginmodel', parent_link=True, auto_created=True, serialize=False, primary_key=True, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('slug', models.SlugField(max_length=254, verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'Carousels',
                'verbose_name': 'Carousel',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CarouselImagePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cms_carousel_carouselimagepluginmodel', parent_link=True, auto_created=True, serialize=False, primary_key=True, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Text', blank=True)),
                ('text', models.TextField(max_length=1000, verbose_name='Text', blank=True)),
                ('image', filer.fields.image.FilerImageField(related_name='carousel_images', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Carousel images',
                'verbose_name': 'Carousel image',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
