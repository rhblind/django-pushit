# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


try:
    from boto import sns
except ImportError:
    raise ImportError("You must install boto in order to use the SNSPushEngine.")

from django.core.exceptions import ImproperlyConfigured

from pushit import logger
from pushit.backends import PushEngine


class SNSPushEngine(PushEngine):
    """

    """

    required_options = ["REGION", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]

    def __init__(self, connection_alias, **options):

        for opt in self.required_options:
            if not opt in options:
                raise ImproperlyConfigured("You must specify '%s' in the connection OPTIONS for "
                                           "this backend." % opt)

        super(SNSPushEngine, self).__init__(connection_alias, **options)
        self.region = options["REGION"]
        self.aws_access_key_id = options["AWS_ACCESS_KEY_ID"]
        self.aws_secret_access_key = options["AWS_SECRET_ACCESS_KEY"]

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
