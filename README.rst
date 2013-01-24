=========================
cmsplugin-simple-markdown
=========================
.. contents:: Table of contents

Simple Markdown plugin is just an simple markdown plugin for django-cms.
It's brutally simple. Just a text area and you'll entered some markdown text and save it.
And the reason why i make this is that, I really couldn't find any simple as stupid plugin
for django-cms, all i've found was fancy with a lot of java script stuff.


Install
=======
``cmsplugin_simple_markdown`` is available at ``pypi``:

http://pypi.python.org/pypi/cmsplugin-simple-markdown

Install it by ``pip``::

    $ python pip install cmsplugin-simple-markdown

Or you can grab the latest version tarball and::

    $ python setup.py install

Then just add it to ``INSTALLED_APPS``.


Drama story
===========
Since every application won't begins with love, this plugin developed to solve a problem.
2 days back, i was using **cms.plugin.text** for handling html pages and stuff, but when I've tried to use aws s3/cloudfront
for my static files, i've stuck with CORS problem.
So i've develop cmsplugin-simple-markdown to be used without any deps on js/css files.
