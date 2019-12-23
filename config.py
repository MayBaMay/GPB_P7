#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY') or '@#qsf!?d/qd&:&039@#:,8'
GOOGLE_JS_KEY = "AIzaSyDcpvFtRDSx4pt3Fuf8etylEYKyUfm9knM"
# GOOGLE_GEO_KEY = os.getenv('GOOGLE_GEO_KEY')

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DeeveloppementConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
