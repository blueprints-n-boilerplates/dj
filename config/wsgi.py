"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

app_path = Path(__file__).parents[1].resolve()
sys.path.append(str(app_path / "apps"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.production")

application = get_wsgi_application()
