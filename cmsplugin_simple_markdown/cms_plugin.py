from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cmsplugin_simple_markdown.models import SimpleMarkdownPlugin

class SimpleMarkdownCMSPlugin(CMSPluginBase):
    model = SimpleMarkdownPlugin
    name = _('Simple Markdown')
    render_template = 'cmsplugin_simple_markdown/simple_markdown.html'

    def render(self, context, instance, placeholder):
        context['text'] = instance.markdown_text
        return context

plugin_pool.register_plugin(SimpleMarkdownCMSPlugin)
