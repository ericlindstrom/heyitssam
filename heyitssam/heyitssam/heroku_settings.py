from settings import *
import os
import dj_database_url

DEBUG = False
DATABASES = {'default': dj_database_url.config(default=os.environ['HEROKU_POSTGRESQL_AMBER_URL'])}
STATIC_URL = '//public.heyitssam.com'
