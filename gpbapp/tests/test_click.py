#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module contains tests on links between server app and the server"""

from flask_testing import LiveServerTestCase
from selenium import webdriver
from .. import app


QUERY_ALL = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? "
QUERY_ALL += "Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le "
QUERY_ALL += "musée d'art et d'histoire de Fribourg, s'il te plaît?"


class AppTest(LiveServerTestCase):
    """This class tests the app"""

    def create_app(self):
        """Create the app with tests configuration"""
        app.config.from_object('app.tests.config')
        return app

    def setUp(self):
        """launch webdriver"""
        self.driver = webdriver.Firefox()

    def tearDown(self):
        """quit web driver after testing"""
        self.driver.quit()

    def get_elt(self, selector):
        """get element from css selector"""
        return self.driver.find_element_by_css_selector(selector)

    def test_url(self):
        """check if opened URL is the one asked in config"""
        self.driver.get(self.get_server_url())
        assert self.driver.current_url == app.config['URL']

    def enter_text_field(self, selector, text):
        """enter a text in the form"""
        # Find user question.
        text_field = self.get_elt(selector)
        # Make sure nothing is in the form.
        text_field.clear()
        # Add the text in the form.
        text_field.send_keys(text)

    def submits_form(self):
        """Submit the form"""
        # Enter question into the form
        self.enter_text_field('#query', QUERY_ALL)
        # submit the form
        self.get_elt('#query').submit()

    def test_user_submition(self):
        """tests if current_url is still the expected one """
        self.driver.get(self.get_server_url())
        self.submits_form()
        assert self.driver.current_url == 'http://localhost:8943/'
