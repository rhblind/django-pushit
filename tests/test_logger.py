# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.test import TestCase

import logging
from pushit.logger import Logger


class LoggerTestCase(TestCase):

    def test_get_default_logger(self):
        from pushit.logger import logger
        try:
            self.assertIsInstance(logger, logging.Logger)
        except AttributeError:
            # Python 2.6, 3.0 and 3.1 does not have assertIsInstance
            assert isinstance(logger, logging.Logger), self.fail()

