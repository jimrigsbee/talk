#!/usr/bin/make -f
# Copyright (c) 2020 Red Hat Training <training@redhat.com>
#
# All rights reserved.
# No warranty, explicit or implied, provided.
#
# You MUST define the PS_PASSWD variable before running that Makefile.
# The variable must be set with the password of the PyPI server.

SHELL=/bin/bash

default: build

clean:
	-rm -rf dist build .eggs

lint:
	flake8 .

build: clean
	python3 setup.py sdist
