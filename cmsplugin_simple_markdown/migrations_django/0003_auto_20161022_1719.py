# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_simple_markdown', '0002_auto_20160417_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplemarkdownplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_simple_markdown_simplemarkdownplugin', primary_key=True, serialize=False, auto_created=True, to='cms.CMSPlugin'),
        ),
    ]
