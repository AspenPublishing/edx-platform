"""
WSGI config for LMS.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments.
It exposes a module-level variable named ``application``. Django's
``runserver`` and ``runfcgi`` commands discover this application via the
``WSGI_APPLICATION`` setting.
"""

# Patch the xml libs
from openedx.core.lib.safe_lxml import defuse_xml_libs

defuse_xml_libs()

import os  # lint-amnesty, pylint: disable=wrong-import-order, wrong-import-position
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms.envs.aws")

from azure.monitor.opentelemetry import configure_azure_monitor
configure_azure_monitor(
    connection_string=os.environ.get("AZURE_CONNECTION_STRING"),
    live_stream=True
)
os.environ.setdefault("PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION", "python")

import lms.startup as startup  # lint-amnesty, pylint: disable=wrong-import-position
startup.run()

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application  # lint-amnesty, pylint: disable=wrong-import-order, wrong-import-position
application = get_wsgi_application()
