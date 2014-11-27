Push notifications for Django made easy!
========================================

Contents:

.. toctree::
   :maxdepth: 2



About
=====
This library attempts to ease the use of push notifications when Django acts as a
backend for mobile apps.

Features
--------
**Python 3 compatible**

**Supported push notification services:**

    - Amazon SNS (Simple Notification Service) (Not implemented yet)
    - APNS (Apple Push Notification Service) (Not implemented yet)
    - GCM (Google Cloud Messaging) (Not implemented yet)
    - MPNS (Microsoft Push Notification Service) (Not implemented yet)

**Familiar syntax**

    Using `pushit` should feel right at home with Django users. Push notifications can be sent from any model
    instance inherited by the `BasePushDevice` class, and messages can be sent to subscription topics by `Queryset`
    instances.

Installation
============
It's in the cheese shop! (Well not yet)

.. code-block:: none

    $ pip install django-pushit

Dependencies
------------
    - Boto (If you want to use AWS SNS)
    - Celery (All requests to external services are executed asynchronously)


Changelog
=========

v1.0
----
*Release date: Not yet released*

Initial release.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

