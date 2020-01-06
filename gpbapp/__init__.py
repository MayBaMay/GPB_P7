#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Initialize the app with Flask"""

from flask import Flask
from config import *

app = Flask(__name__)
app.config.from_object('config')

from gpbapp import views

print("clé ", os.getenv("GOOGLE_GEO_K"))
