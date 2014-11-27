# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

try:
    from boto import sns
except ImportError:
    raise ImportError("You must install boto in order to use the SNSPushBackend.")

from pushit import Logger
from pushit.backends import PushBackend


class SNSPushBackend(PushBackend):
    """

    """

    required_options = ["REGION", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]

    def __init__(self, connection_alias, **settings):
        super(SNSPushBackend, self).__init__(connection_alias, **settings)
        self.logger = Logger.get_logger("pushit.sns")
        self._connection = None

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, connection):
        self._connection = connection

    def connect(self):
        self.connection = sns.connect_to_region(
            region_name=self.region, aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )
        return self.connection
