import threading
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from cmsplugin_simple_markdown import utils


localdata = threading.local()
localdata.TEMPLATE_CHOICES = utils.autodiscover_templates()
TEMPLATE_CHOICES = localdata.TEMPLATE_CHOICES


class SimpleMarkdownPlugin(CMSPlugin):
    markdown_text = models.TextField(verbose_name=_('text'))
    template = models.CharField(
        verbose_name=_('template'),
        choices=TEMPLATE_CHOICES,
        max_length=255,
        default='cmsplugin_simple_markdown/simple_markdown.html',
        editable=len(TEMPLATE_CHOICES) > 1
    )

    def __unicode__(self):
        return self.markdown_text
