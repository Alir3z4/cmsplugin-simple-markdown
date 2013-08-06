import glob
import os
import threading
from django.conf import settings

localdata = threading.local()
localdata.TEMPLATES = tuple()
TEMPLATES = localdata.TEMPLATES


def autodiscover_templates():
    """
    Autodiscover `cmsplugin_simple_markdown` templates the way
    'django.template.loaders.filesystem.Loader' and
    'django.template.loaders.app_directories.Loader' work.
    """
    def sorted_templates(templates):
        """
        Sort templates.
        """
        TEMPLATES = sorted(templates, key=lambda template: template[1])
        return TEMPLATES

    # obviously, cache for better performance
    global TEMPLATES
    if TEMPLATES:
        return TEMPLATES

    # Override templates from settings
    override_dir = getattr(settings, 'CMSPLUGIN_SIMPLE_MARKDOWN_TEMPLATES', None)
    if override_dir:
        return sorted_templates(override_dir)

    templates = []

    dirs_to_scan = []
    if ('django.template.loaders.app_directories.Loader' in
            settings.TEMPLATE_LOADERS):
        for app in settings.INSTALLED_APPS:
            _ = __import__(app)
            tdir = os.path.dirname(_.__file__)
            if not tdir in dirs_to_scan:
                # Append `templates` for app directories
                dirs_to_scan.append(os.path.join(tdir, 'templates'))

    if ('django.template.loaders.filesystem.Loader' in
            settings.TEMPLATE_LOADERS):
        for tdir in settings.TEMPLATE_DIRS:
            if not tdir in dirs_to_scan:
                # File-System loader assumes our templates in
                # `templates` already.
                dirs_to_scan.append(tdir)

    for tdir in dirs_to_scan:
        found = glob.glob(os.path.join(tdir, 'cmsplugin_simple_markdown/*.html'))
        for tfile in found:
            tdir, tfile = os.path.split(tfile)
            k, v = os.path.join(tdir.split('/')[-1], tfile), tfile
            f = False
            for _, template in templates:
                if template == tfile:
                    f = True

            if not f:
                templates.append((k, v))

    return sorted_templates(templates)
