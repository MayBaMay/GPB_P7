#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import .env as env


SECRET_KEY = os.environ.get('SECRET_KEY') or '@#qsf!?d/qd&:&039@#:,8'
GOOGLE_JS_KEY = env.GOOGLE_JS_KEY
GOOGLE_GEO_KEY = env.GOOGLE_GEO_KEY
