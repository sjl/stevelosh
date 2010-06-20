import os

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

import hydeengine
HYDE_FOLDER = os.path.dirname(os.path.dirname(hydeengine.__file__))

LAYOUT_DIR = os.path.join(ROOT_PATH, 'layout')
CONTENT_DIR = os.path.join(ROOT_PATH, 'content')
MEDIA_DIR = os.path.join(ROOT_PATH, 'media')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')
TMP_DIR = os.path.join(ROOT_PATH, 'deploy_tmp')
BACKUPS_DIR = os.path.join(ROOT_PATH, 'backups')

BACKUP = False
DEBUG = True

SITE_ROOT = "/"
SITE_WWW_URL = "http://stevelosh.com"
SITE_NAME = "Steve Losh"
SITE_AUTHOR = "Steve Losh"

GENERATE_ABSOLUTE_FS_URLS = False
GENERATE_CLEAN_URLS = True
LISTING_PAGE_NAMES = ['index']
APPEND_SLASH = True

# {folder : extension : (processors)}
# The processors are run in the given order and are chained.
# Only a lone * is supported as an indicator for folders. Path 
# should be specified. No wildcard card support yet.
 
# Starting under the media folder. For example, if you have media/css under 
# your site root,you should specify just css. If you have media/css/ie you 
# should specify css/ie for the folder name. css/* is not supported (yet).

# Extensions do not support wildcards.

MEDIA_PROCESSORS = {
    '*': {
        '.less': ('hydeengine.media_processors.LessCSS',),
        '.js': ('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.YUICompressor',)
    },
    'images/': {
        '.png': ('hydeengine.media_processors.Thumbnail',),
        '.jpg': ('hydeengine.media_processors.Thumbnail',),
    }
}

CONTENT_PROCESSORS = {}

SITE_PRE_PROCESSORS = {
    'blog': {
        'hydeengine.site_pre_processors.CategoriesManager': {},
    },
    'projects': {
        'hydeengine.site_pre_processors.CategoriesManager': {},
    },
    '/': {
        'hydeengine.site_pre_processors.NodeInjector' : {
            'variable': 'blog_node',
            'path': 'content/blog',
        }
    }
}

SITE_POST_PROCESSORS = {
    # 'media/js': {
    #        'hydeengine.site_post_processors.FolderFlattener' : {
    #                'remove_processed_folders': True,
    #                'pattern':"*.js"
    #        }
    #    }
}

CONTEXT = {
    'GENERATE_CLEAN_URLS': GENERATE_CLEAN_URLS,
    'links': {
        'python': 'http://python.org/',
        'django': 'http://www.djangoproject.com/',
        'cherrypy': 'http://cherrypy.org/',
        'hyde': 'http://github.com/lakshmivyas/hyde/',
        'markdown': 'http://daringfireball.net/projects/markdown/',
        'fabric': 'http://fabfile.org/',
        'blatter': 'http://bitbucket.org/jek/blatter/',
        'webfaction': 'http://www.webfaction.com?affiliate=sjl',
        'mercurial': 'http://mercurial.selenic.com/',
        'git': 'http://git-scm.com/',
        'aardvarklegs': 'http://fecklessmind.com/2009/01/20/aardvark-css-framework/',
        'hgtip': 'http://hgtip.com/',
        'lesscss': 'http://lesscss.org/',
        'bitbucket': 'http://bitbucket.org/',
        'github': 'http://github.com/',
    },
}

FILTER = { 
    'include': (".htaccess",),
    'exclude': (".*","*~")
}        


# Processor Configuration

YUI_COMPRESSOR = os.path.join(HYDE_FOLDER, 'lib', 'yuicompressor-2.4.1.jar')
HSS_PATH = None # if you don't want to use HSS
LESS_CSS_PATH = '/Users/sjl/.gem/ruby/1.8/bin/lessc'
THUMBNAIL_MAX_WIDTH = 140
THUMBNAIL_MAX_HEIGHT = 300
THUMBNAIL_FILENAME_POSTFIX = '-thumb'

# Django settings

TEMPLATE_DIRS = (LAYOUT_DIR, CONTENT_DIR, TMP_DIR, MEDIA_DIR)
INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
)
