# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from pushit.constants import DEFAULT_ALIAS
from pushit.logger import Logger
from pushit.utils import loading


# Set up a logger for the app
logger = Logger.get_logger(name="pushit")

if not hasattr(settings, "PUSHIT_CONNECTIONS"):
    raise ImproperlyConfigured("The 'PUSHIT_CONNECTIONS' setting is required.")
if not DEFAULT_ALIAS in settings.PUSHIT_CONNECTIONS:
    raise ImproperlyConfigured("The default alias '%s' must be included in the PUSHIT_CONNECTIONS setting." % DEFAULT_ALIAS)


# Load the connections
connections = loading.ConnectionHandler(settings.PUSHIT_CONNECTIONS)
