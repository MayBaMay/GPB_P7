#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Configuration script for tests purposes """

import os

SECRET_KEY_TEST = os.environ.get('SECRET_KEY') or '@#qsf!?d/qd&:&039@#:,8'
GOOGLE_KEY_TEST = os.environ.get("GOOGLE_GEO_KEY")


URL = "http://localhost:8943/"

DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10
