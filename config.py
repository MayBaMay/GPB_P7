#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from boto.s3.connection import S3Connection

SECRET_KEY = os.environ.get('SECRET_KEY') or '@#qsf!?d/qd&:&039@#:,8'
GOOGLE_JS_KEY = "AIzaSyDcpvFtRDSx4pt3Fuf8etylEYKyUfm9knM"
GOOGLE_GEO_KEY = os.environ.get('GOOGLE_GEO_KEY')
