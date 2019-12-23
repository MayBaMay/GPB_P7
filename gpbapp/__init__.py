#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Initialize the app with Flask"""

from flask import Flask
from config import *

app = Flask(__name__)
app.config.from_object('Config')
app.config.from_envvar('GOOGLE_GEO_KEY')

from gpbapp import views
