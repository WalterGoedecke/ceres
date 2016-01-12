"""
WSGI config for solocalc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

PROJECT_APP_PATH = os.path.abspath(os.path.split(__file__)[0])
root_path = os.path.dirname(PROJECT_APP_PATH)
sys.path.insert(0, root_path)
#f = open("/home/solarfs/webapps/solocalc_app/solocalc/test.txt","w") 
#f.write("root_path = %s\n" % root_path)
#PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
#f.write("PROJECT_APP_PATH = %s\n" % PROJECT_APP_PATH)
#f.write("next root_path = %s\n" % root_path)

#sys.path.insert(0, '/home/solarfs/webapps/solocalc_app/solocalc')

from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("solocalc"))

settings_module = "%s.settings" % real_project_name("solocalc")
#f = open("/home/solarfs/webapps/solocalc_app/solocalc/DJANGO_SETTINGS_MODULE.txt","w") 
#f.write("next root_path = %s\n" % root_path)
#f.write("DJANGO_SETTINGS_MODULE set to: %s\n" % settings_module)
#f.close() 

application = get_wsgi_application()
