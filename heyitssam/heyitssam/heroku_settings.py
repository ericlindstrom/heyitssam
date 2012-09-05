from settings import *
import os
import dj_database_url

DEBUG = False
DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ['S3_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET'] 
AWS_STORAGE_BUCKET_NAME = 'public.heyitssam.com'

STATIC_URL = '//%s/static/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s/media/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = '//%s/admin/' % AWS_STORAGE_BUCKET_NAME

