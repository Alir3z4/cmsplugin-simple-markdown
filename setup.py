from setuptools import setup, find_packages

setup(
    name='cmsplugin_simple_markdown',
    version=".".join(map(str, __import__('cmsplugin_simple_markdown').__version__)),
    packages=[find_packages(exclude='django_cmsplugin_simple_markdown')],
    url='https://www.github.com/Alir3z4/cmsplugin-simple-markdown',
    license='BSD',
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    description='A plugin for django-cms which provides just a markdown plugin and nothing more.',
    install_requires=['django', 'django-cms', 'markdown'],
    keywords=[
        'django',
        'request',
        'web'
    ],
    platforms='OS Independent',
    provides=['cmsplugin_simple_markdown',],
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
