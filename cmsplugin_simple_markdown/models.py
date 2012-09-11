from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

class SimpleMarkdownPlugin(CMSPlugin):
    markdown_text = models.TextField(verbose_name=_('markdown body'))

    def __unicode__(self):
        return self.markdown_text
