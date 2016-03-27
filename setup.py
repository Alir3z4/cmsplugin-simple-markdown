from setuptools import setup

setup(
    name='cmsplugin-simple-markdown',
    version=".".join(map(str, __import__('cmsplugin_simple_markdown').__version__)),
    packages=['cmsplugin_simple_markdown', 'cmsplugin_simple_markdown.migrations', 'cmsplugin_simple_markdown.migrations_django'],
    package_dir={'cmsplugin_simple_markdown': 'cmsplugin_simple_markdown'},
    package_data={'cmsplugin_simple_markdown': ['templates/*/*']},
    install_requires=[
        'django',
        'markdown',
        'django-markdown',
        'django-cms'
    ],
    url='https://www.github.com/Alir3z4/cmsplugin-simple-markdown',
    license=open('LICENSE').read(),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    description='A plugin for django-cms that provides just a markdown plugin and nothing more.',
    long_description=open('README.rst').read(),
    keywords=[
        'django',
        'django-cms',
        'web',
        'cms',
        'cmsplugin',
        'plugin',
    ],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development'
    ],
)
