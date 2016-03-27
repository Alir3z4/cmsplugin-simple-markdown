# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleMarkdownPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('markdown_text', models.TextField(verbose_name='text')),
                ('template', models.CharField(default=b'cmsplugin_simple_markdown/simple_markdown.html', verbose_name='template', max_length=255, editable=False, choices=[(b'cmsplugin_simple_markdown/simple_markdown.html', b'simple_markdown.html')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
