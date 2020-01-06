#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module contains the view functions responding to requests to the application."""

from flask import render_template, request, jsonify
from gpbapp import app
from .utils.grandpy import GrandPy
from .utils.parser import Parser
from .utils.google_api import GoogleApi
from .utils.wiki_api import WikimediaApi

@app.route('/')
@app.route('/index/')
def index():
    """Render template index with sentence grandPyBot and googlemap's key"""
    grandpy = GrandPy()
    return render_template('index.html',
                           presentation=grandpy.presentation,
                           gmap_api_key=app.config['GOOGLE_JS_KEY'])

@app.route('/process', methods=['POST'])
def process():
    """get user input and return response
    This route is called with AJAX when user submit the form"""
    # generate new GrandPy instance for each request to get new random answer
    grandpy = GrandPy()
    # get input from user
    user_input = request.form['user_input']
    # parse it
    parser = Parser(user_input)

    #########################################
    ####### find query in google API ########
    #########################################
    # try parsed query as words after key words
    query = parser.parsed_after_keyword
    google = GoogleApi(query)
    # if google find with those words, response attribute is True
    if google.response:
        geoloc = "{} {}".format(grandpy.geo_answer, google.address)
    # else those words don't respond, use words before key words
    else:
        query = parser.parsed_before_keyword
        google = GoogleApi(query)
        # same proceed if google Api found it response is True
        if google.response:
            geoloc = "{} {}".format(grandpy.geo_answer,
                                    google.address)
        # else new attempt failed as well, granpy can't help you so give a geo_noresults_answer
        else:
            geoloc = "{}".format(grandpy.geo_noresults_answer)

    #########################################
    ###### find query in mediawiki API ######
    #########################################
    # if grandpy doesn't know where it is, he can't talk about it
    if google.response:
        wiki = WikimediaApi(query, google.latitude, google.longitude)
        if wiki.response:
            story = "{} {}".format(grandpy.wiki_answer, wiki.content)
        else:
            story = "{}".format(grandpy.wiki_noresults_answer)
    else:
        story = "{}".format(grandpy.wiki_noresults_answer)

    #########################################
    ########### return response #############
    #########################################
    return jsonify(response=google.response,
                   geoloc=geoloc,
                   key=app.config['GOOGLE_JS_KEY'],
                   lat=google.latitude,
                   lng=google.longitude,
                   story=story)


if __name__ == "__main__":
    app.run()
