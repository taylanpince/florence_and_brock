import os
import sys

sys.path.append('/home/florencebrockteam/site/florence_and_brock/build')
sys.path.append('/home/florencebrockteam/site/florence_and_brock/build/libs')
sys.path.append('/home/florencebrockteam/site/florence_and_brock/build/florence_and_brock')

os.environ['DJANGO_SETTINGS_MODULE'] = 'florence_and_brock.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()