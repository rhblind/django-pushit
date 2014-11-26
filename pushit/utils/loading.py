# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.utils import importlib


def import_class(path):
    bits = path.split(".")
    class_name = bits.pop()
    module_name = ".".join(bits)
    module = importlib.import_module(module_name)

    if not hasattr(module, class_name):
        raise ImportError("The Python module '%s' has no '%s' class." % (module_name, class_name))

    return getattr(module, class_name)


def load_backend(backend_path):
    """
    Loads a backend for sending push notifications.

    Requires a ``backend_path`` which is a string resembeling a Python import
    path, pointing to a ``PushEngine`` subclass. The build-in options available
    includes:

        * pushit.backends.apns.APNSPushEngine (Apple Push Notification Service)
        * pushit.backends.gcm.GCMPushEngine (Google Cloud Messaging)
        * pushit.backends.mpns.MPNSPushEngine (Microsoft Push Notification Service)
        * pushit.backend.sns.SNSPushEngine (Simple Notification Service)
    """

    bits = backend_path.split(".")
    if len(bits) < 2:
        raise ImproperlyConfigured("The configured backend '%s' is not a complete Python path to "
                                   "a PushEngine subclass." % backend_path)

    return import_class(backend_path)


class ConnectionHandler(object):
    def __init__(self, connection_settings):
        self.connection_settings = connection_settings
        self._connections = {}

    def ensure_defaults(self, alias):
        try:
            settings = self.connection_settings[alias]
        except KeyError:
            raise ImproperlyConfigured("The key '%s' isn't an available connection." % alias)

        # Depending on what backend the user has chosen,
        # we should do some checks to make sure that all available options
        # has been provided.
        # EDIT: Nope, that's the backends responsiblity!

    def __getitem__(self, alias):
        if alias in self._connections:
            return self._connections[alias]

        self.ensure_defaults(alias)
        self._connections[alias] = load_backend(self.connection_settings[alias]["ENGINE"])(using=alias)
        return self._connections[alias]

    def __setitem__(self, alias, connection):
        setattr(self._connections, alias, connection)

    def __iter__(self):
        return iter(self._connections)

    def all(self):
        return [self[alias] for alias in self.connection_settings]
