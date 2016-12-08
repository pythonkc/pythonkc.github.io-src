#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The PythonKC Organizer Team'
SITENAME = 'PythonKC'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Theme
THEME = 'pelican-bootstrap3'
SIDEBAR_DIGEST = 'supporting the Python community in the greater Kansas City area'
TWITTER_USERNAME = 'pythonkc'
PYGMENTS_STYLE = 'solarizedlight'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('PyKC Meetup.com', 'https://www.meetup.com/pythonkc/'),
    ('PyKC Slack', 'https://pykc-slackipy.herokuapp.com/'),
    ('Pelican', 'http://docs.getpelican.com/en/stable/'),
    ('Python.org', 'https://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/PythonKC'),
    ('GitHub', 'https://github.com/pythonkc'),
    ('LinkedIn', 'https://www.linkedin.com/groups/3996011'),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
