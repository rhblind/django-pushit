# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.utils import six


class PushBackend(object):
    """
    Base class for PushEngines
    """

    required_options = []

    def __init__(self, connection_alias, **settings):
        if not "OPTIONS" in settings:
            raise ImproperlyConfigured("You must specify 'OPTIONS' in the connection settings.")

        for opt in self.required_options:
            if not opt in settings["OPTIONS"]:
                raise ImproperlyConfigured("You must specify '%s' in the connection OPTIONS for "
                                           "this backend." % opt)

        for key, val in six.iteritems(settings["OPTIONS"]):
            setattr(self, key.lower(), val)
        self.connection_alias = connection_alias
