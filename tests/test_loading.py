# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ImproperlyConfigured

from django.test import TestCase
from pushit.utils import loading


class ConnectionHandlerTestCase(TestCase):

    def test_init(self):
        conn_handler = loading.ConnectionHandler({})
        self.assertEqual(conn_handler.connection_settings, {})
        self.assertEqual(conn_handler._connections, {})

        conn_handler = loading.ConnectionHandler({
            "default": {
                "ENGINE": "pushit.backends.PushBackend",
                "OPTIONS": {}
            }
        })
        self.assertEqual(conn_handler.connection_settings, {
            "default": {
                "ENGINE": "pushit.backends.PushBackend",
                "OPTIONS": {}
            }
        })
        self.assertEqual(conn_handler._connections, {})

    def test_get_item(self):
        conn_handler = loading.ConnectionHandler({})

        try:
            empty_backend = conn_handler["default"]
            self.fail()
        except ImproperlyConfigured:
            pass

        conn_handler = loading.ConnectionHandler({
            "default": {
                "ENGINE": "pushit.backends.PushBackend",
                "OPTIONS": {}
            }
        })
        sns_backend = conn_handler["default"]
        backend_path, memory_addr = repr(sns_backend).strip("<>").split(" object at ")
        self.assertEqual(backend_path, "pushit.backends.PushBackend")

        # Make sure we're loading out of the memorized connection.
        sns_backend2 = conn_handler["default"]
        backend_path2, memory_addr2 = repr(sns_backend2).strip("<>").split(" object at ")
        self.assertEqual(backend_path2, "pushit.backends.PushBackend")
        self.assertEqual(memory_addr, memory_addr2)

        try:
            empty_backend = conn_handler["foobar"]
            self.fail()
        except ImproperlyConfigured as e:
            self.assertEqual(str(e), "The key 'foobar' isn't an available connection.")

    def test_iter_connections(self):
        conn_handler = loading.ConnectionHandler({
            "default": {
                "ENGINE": "pushit.backends.PushBackend",
                "OPTIONS": {}
            },
            "secondary": {
                "ENGINE": "pushit.backends.PushBackend",
                "OPTIONS": {}
            }
        })

        # Make sure we can iterate over the class instance
        from collections import Iterable

        iterable = iter(conn_handler)
        assert isinstance(iterable, Iterable), self.fail()

        # Make sure the connection handler contains the expected number of items
        self.assertEqual(len(conn_handler.all()), 2)


class ImportClassTestCase(TestCase):

    def test_load_existing_path(self):
        backend = loading.import_class("pushit.backends.PushBackend")
        self.assertEqual(backend.__name__, "PushBackend")

    def test_load_nonexisting_path(self):
        self.assertRaises(ImportError, loading.import_class, "pushit.backends.FooBackend")
