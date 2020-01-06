#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

load_dotenv() # load variables from file .env
GOOGLE_GEO_KEY = os.getenv("GOOGLE_GEO_K")
GOOGLE_JS_KEY = os.getenv("GOOGLE_JS_K")

SECRET_KEY = os.environ.get('SECRET_KEY') or '@#qsf!?d/qd&:&039@#:,8'
