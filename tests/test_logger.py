# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import logging
from django.test import TestCase


class LoggerTestCase(TestCase):

    def test_get_default_logger(self):
        from pushit.logger import logger
        assert isinstance(logger, logging.Logger), self.fail()

    def test_get_named_logger(self):
        from pushit.logger import Logger
        logger = Logger.get_logger(name="pushit_test_logger")
        assert isinstance(logger, logging.Logger), self.fail()
