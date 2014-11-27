# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from pushit.backends import PushBackend


class APNSPushBackend(PushBackend):
    """

    """

    def __init__(self, connection_alias, **options):
        super(APNSPushBackend, self).__init__(connection_alias, **options)
        raise NotImplementedError()
