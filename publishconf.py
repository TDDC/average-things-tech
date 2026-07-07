# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://tddc.github.io/average-things-tech"
INDEX_SAVE_AS = 'blog/index.html'
RELATIVE_URLS = False

MENUITEMS = [
    ('Home', f'{SITEURL}/'),
    ('Start Here', f'{SITEURL}/start-here/'),
    ('Guides', f'{SITEURL}/guides/'),
    ('Articles', f'{SITEURL}/articles/'),
    ('Open Letters', f'{SITEURL}/open-letters/'),
    ('White Papers', f'{SITEURL}/white-papers/'),
    ('About', f'{SITEURL}/about/'),
]

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
