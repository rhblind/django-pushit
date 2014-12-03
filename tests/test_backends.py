# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import warnings
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from pushit.utils import loading


class LoadBackendTestCase(TestCase):

    def test_load_base_push_backend(self):
        backend = loading.load_backend("pushit.backends.PushBackend")
        self.assertEqual(backend.__name__, "PushBackend")

    def test_load_apns_backend(self):
        backend = loading.load_backend("pushit.backends.apns.APNSPushBackend")
        self.assertEqual(backend.__name__, "APNSPushBackend")

    def test_load_gcm_backend(self):
        backend = loading.load_backend("pushit.backends.gcm.GCMPushBackend")
        self.assertEqual(backend.__name__, "GCMPushBackend")

    def test_load_mpns_backend(self):
        backend = loading.load_backend("pushit.backends.mpns.MPNSPushBackend")
        self.assertEqual(backend.__name__, "MPNSPushBackend")

    def test_load_sns_backend(self):
        try:
            import boto
        except ImportError:
            warnings.warn("Boto doesn't appear to be installed. Unable to test loading the SNS backend.")
            return

        backend = loading.load_backend("pushit.backends.sns.SNSPushBackend")
        self.assertEqual(backend.__name__, "SNSPushBackend")

    def test_load_nonexistent(self):
        self.assertRaises(ImproperlyConfigured, loading.load_backend, "foobar")
        self.assertRaises(ImportError, loading.load_backend, "foo.BARPushBackend")
