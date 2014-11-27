# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import os
from tempfile import mkdtemp


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

SECRET_KEY = "NOBODY expects the Spanish Inquisition!"

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "pushit",
    # "tests.core_test"

)

SITE_ID = 1
ROOT_URLCONF = "tests.core.urls"

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

PUSHIT_CONNECTIONS = {
    "default": {
        "ENGINE": "pushit.backends.sns.SNSPushBackend",
        "OPTIONS": {
            "REGION": "eu-west-1",
            "AWS_ACCESS_KEY_ID": "Read from os.env",
            "AWS_SECRET_ACCESS_KEY": "Read from os.env",
            "APPLICATION_ARN": "dwdw"
        }
    }
}
