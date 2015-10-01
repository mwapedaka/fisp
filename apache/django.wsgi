import os, sys

sys.path.append('C:/fisp/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'fisp.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()