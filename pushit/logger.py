# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import logging
from django.utils.log import dictConfig


class Logger(object):
    """
    Global logger class.
    Unless ``logger_name`` is configured in settings.py, this creates a default console logger.
    """

    logger = None
    logger_name = "default"

    @classmethod
    def get_logger(cls, name=None):
        """
        Sets up a default DEBUG console logger if no other logger
        is configured.

        :rtype : object
        """
        if name is not None:
            cls.logger_name = name

        if cls.logger is None:
            dictConfig({
                "version": 1,
                "disable_existing_loggers": False,
                "formatters": {
                    "verbose": {
                        "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
                    },
                },
                "handlers": {
                    "console": {
                        "level": "DEBUG",
                        "class": "logging.StreamHandler",
                        "formatter": "verbose"
                    },
                },
                "loggers": {
                    cls.logger_name: {
                        "level": "DEBUG",
                        "handlers": ["console"],
                        "propagate": False
                    }
                }
            })
            cls.logger = logging.getLogger(cls.logger_name)

        return cls.logger


if hasattr(logging, "captureWarnings"):  # pragma: no cover
    logging.captureWarnings(True)

# Global logger
logger = Logger.get_logger(name="pushit")
