#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
# from dotenv import load_dotenv

#### get GOOGLE_GEO_KEY depending if running in localhost or heroku
try:
    load_dotenv()
    GOOGLE_GEO_KEY = os.getenv("GOOGLE_GEO_K")
    print(GOOGLE_GEO_KEY + "local")
except:
    # GOOGLE_GEO_KEY = os.environ.get('GOOGLE_GEO_K')
    # print(GOOGLE_GEO_KEY)
    GOOGLE_GEO_KEY = os.popen('heroku config:get GOOGLE_GEO_K').readlines()
    GOOGLE_GEO_KEY = GOOGLE_GEO_KEY[0][1:40]

# if running with heroku, 'IS_HEROKU' would be True
# is_prod = os.environ.get('IS_HEROKU', None)

# if is_prod:
#     GOOGLE_GEO_KEY = os.environ.get('GOOGLE_GEO_K')
# else:
#     from dotenv import load_dotenv
#     load_dotenv()
#     GOOGLE_GEO_KEY = os.getenv("GOOGLE_GEO_K")


SECRET_KEY = os.environ.get('SECRET_KEY') or '@#qsf!?d/qd&:&039@#:,8'
GOOGLE_JS_KEY = "AIzaSyDcpvFtRDSx4pt3Fuf8etylEYKyUfm9knM" # this key has a Website restrictions
