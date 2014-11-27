# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


class PushEngine(object):
    """
    Base class for PushEngines
    """

    def __init__(self, connection_alias, **options):
        self.connection_alias = connection_alias
