=========================
cmsplugin-simple-markdown
=========================
.. contents:: Table of contents

Simple Markdown plugin is just an simple markdown plugin for django-cms.
It's brutally simple. Just a text area and you'll entered some markdown text and save it.
And the reason why i make this is that, I really couldn't find any simple as stupid plugin
for django-cms, all i've found was fancy with a lot of java script stuff.




Installation
==============

PyPi
-----

**cmsplugin-simple-markdown** is available on PyPi:

http://pypi.python.org/pypi/cmsplugin-simple-markdown
::

    $ pip install cmsplugin-simple-markdown

Git
---

You can get latest stable changes from github server:
::

    $ git clone https://github.com/Alir3z4/cmsplugin-simple-markdown.git
    $ cd cmsplugin-simple-markdown
    $ python setup.py install

Zip, Tarball
------------

You can grab the latest tarball.

*unix
------

Get the latest tarball & install
::

    $ wget https://github.com/Alir3z4/cmsplugin-simple-markdown/archive/master.tar.gz
    $ tar xvzf cmsplugin-simple-markdown-master.tar.gz && cd cmsplugin-simple-markdown-master
    $ python setup.py install

Windows
-------

Download latest zip archive.

https://github.com/Alir3z4/cmsplugin-simple-markdown/archive/master.zip

Extract the archive, and run the following command in root directory of cmsplugin-simple-markdown
::

    $ python setup.py install

Configuration
==============

Most people says that installation of cmsplugin-simple-markdown is easy, Seems they're out of space.
It's fucking hard to install.

Configuration & Usage
----------------------

1. Add ``cmsplugin_simple_markdown`` to  ``INSTALLED_APPS``.
2. Add ``django.contrib.markup`` to ``INSTALLED_APPS``, if it isn't included already.
3. Create the database tables::

    $ python manage.py migrate


This is not easy, It's hard, confusing. I doubt, double doubt that those people that keep saying installing this
is easy are on something.


Drama story
===========
Since every application won't begins with love, this plugin developed to solve a problem.
2 days back, I've been using **cms.plugin.text** for handling html pages and related content,
but when I've tried to use aws s3/cloudfront for my static files, i've stuck with ``CORS`` problem.
So i've develop ``cmsplugin-simple-markdown`` to be used without any deps on js/css files.

Now these days, people all around the world are using it, They are happy with it, They go creazy with ``cmsplugin-simple-markdown``,  
Even they name their child ``cmsplugin-simple-markdown``, At least I did. ;)
