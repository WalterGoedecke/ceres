#!/home2/snowbear/python34/bin/python3.4
# /home2/snowbear/python/bin/python2.7

import sys, os
 
# Add a custom Python path.
#sys.path.insert(0, "/home2/snowbear/python/lib/python2.7/site-packages")
sys.path.insert(0, "/home2/snowbear/python34/lib/python3.4/site-packages")
sys.path.append("/home2/snowbear/django_projects/memorial")
sys.path.append("/home2/snowbear/django_projects")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "memorial.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")

