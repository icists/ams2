"""
WSGI config for ams2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "ams2.settings"
# os.environ["UWSGI_ROUTE_HOST"] = "`^(?!localhost$) break:400"

application = get_wsgi_application()
