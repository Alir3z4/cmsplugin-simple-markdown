from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

class SimpleMarkdownPlugin(CMSPlugin):
    mardown_text = models.TextField(verbose_name=_('markdown body'))

    def __unicode__(self):
        return self.mardown_text
