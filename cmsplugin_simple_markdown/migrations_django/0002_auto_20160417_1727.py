# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_simple_markdown', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplemarkdownplugin',
            name='template',
            field=models.CharField(choices=[('cmsplugin_simple_markdown/simple_markdown.html', 'simple_markdown.html')], max_length=255, editable=False, verbose_name='template', default='cmsplugin_simple_markdown/simple_markdown.html'),
        ),
    ]
