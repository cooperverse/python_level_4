"""
WSGI config for Md_Jahedul_Kawser_10_Portpolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Md_Jahedul_Kawser_10_Portpolio.settings')

application = get_wsgi_application()
