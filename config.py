#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os


try:
    from dotenv import load_dotenv
    load_dotenv()
    GOOGLE_GEO_KEY = os.getenv("GOOGLE_GEO_KEY")
except ImportError:
    GOOGLE_GEO_KEY = os.environ.get('GOOGLE_GEO_KEY')


SECRET_KEY = os.environ.get('SECRET_KEY') or '@#qsf!?d/qd&:&039@#:,8'
GOOGLE_JS_KEY = "AIzaSyDcpvFtRDSx4pt3Fuf8etylEYKyUfm9knM" # this key has a Website restrictions
