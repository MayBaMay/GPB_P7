#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

#### get GOOGLE_GEO_KEY depending if running in localhost or heroku
try:    # try to load local variables from file .env
    load_dotenv()
    DEBUG = True
except:  # if fails it's production mode and debug is False
    DEBUG = False

# in each case google api keys should be in environnement variables
GOOGLE_GEO_KEY = os.getenv("GOOGLE_GEO_K")
GOOGLE_JS_KEY = os.getenv("GOOGLE_JS_K")

SECRET_KEY = os.environ.get('SECRET_KEY') or '@#qsf!?d/qd&:&039@#:,8'
