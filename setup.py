# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="django-pushit",
    version="1.0",
    description="Push notifications for Django",
    long_description=open("README.rst", "r").read(),
    author="Rolf Håvard Blindheim",
    author_email="rhblind@gmail.com",
    url="https://github.com/rhblind/django-pushit",
    download_url="https://github.com/rhblind/django-pushit.git",
    license="The MIT License (MIT)",
    packages=[
        "pushit",
        "pushit.backends",
        "pushit.migrations",
        "pushit.utils"
    ],
    include_package_data=True,
    install_requires=[
        "Django>=1.5.0",
        "celery"
    ],
    tests_require=[
        "nose",
        "mock",
        "coverage"
    ],
    zip_safe=False,
    test_suite="tests.run_tests.start",
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]

)
