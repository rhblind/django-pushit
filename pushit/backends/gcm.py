# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from pushit.backends import PushBackend


class GCMPushBackend(PushBackend):
    """
    https://developer.android.com/google/gcm/index.html
    """

    def __init__(self, connection_alias, **options):
        super(GCMPushBackend, self).__init__(connection_alias, **options)
        raise NotImplementedError()
