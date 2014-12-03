# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from pushit import logger
from pushit import connections


class LoadPushitTestCase(TestCase):

    def test_has_logger(self):
        import logging
        assert isinstance(logger, logging.Logger), self.fail()

    def test_logger_name(self):
        self.assertEqual(logger.name, "pushit")

    def test_has_connections(self):
        from pushit.utils import loading
        assert isinstance(connections, loading.ConnectionHandler), self.fail()

