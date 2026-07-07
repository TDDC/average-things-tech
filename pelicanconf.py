AUTHOR = 'Zaran Hirachand Dhulla'
SITENAME = 'Average Things Tech'
SITEURL = ""

PATH = "content"

ARTICLE_PATHS = ['articles', 'episodes', 'guides', 'open-letters', 'white-papers', 'big-ideas']
PAGE_PATHS = ['pages', 'notes']
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            
        },
    },
    'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu settings
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ('Home', '/'),
    ('Start Here', '/start-here/'),
    ('Guides', '/guides/'),
    ('Articles', '/articles/'),
    ('Big Ideas', '/big-ideas/'),
    ('Open Letters', '/open-letters/'),
    ('White Papers', '/white-papers/'),
    ('About', '/about/'),
]

# Blogroll
LINKS = []

# Social widget
SOCIAL = []

DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True

# Move default article listing away from homepage
# The custom homepage will be generated from content/pages/home.md as index.html
INDEX_SAVE_AS = 'blog/index.html'

# Uncomment following line if you want document-relative URLs when developing

# Clean URL structure
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Local development URLs
RELATIVE_URLS = True
