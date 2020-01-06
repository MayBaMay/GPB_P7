#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module contains tests of GooglesAPI's and MediaWiki API's results"""

import json
import requests
from ..utils.google_api import GoogleApi
from ..utils.wiki_api import WikimediaApi


class MockResponse:
    """Class creating a MockResponse object"""
    def __init__(self, file):
        self.file = file

    def json(self):
        """method of the MockResponse object with the mockResponse in json format"""
        with open(self.file, "r") as file:
            json_results = json.load(file)
        return json_results


class TestGoogle:
    """This class contains tests on GoogleAPI's results"""

    def test_resquest_datas_in_json(self, monkeypatch):
        """This method tests how class GoogleApi get datas from Google API requests"""
        # https://docs.pytest.org/en/latest/monkeypatch.html

        def mock_get(*args, **kwargs):
            """Get the mock from MockResponse class"""
            return MockResponse("gpbapp/tests/tests_helpers/google_mock_result.json")

        # apply the monkeypatch for requests.get to mock_get
        monkeypatch.setattr(requests, "get", mock_get)

        # method .get_infos_from_query, which contains requests.get, uses the monkeypatch
        test = GoogleApi('Tour Eiffel')
        assert test.query_datas["candidates"][0]["name"] == "Tour Eiffel"
        assert test.infos["address"] == "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France"
        assert test.response

    def test_not_found_in_google(self, monkeypatch):
        """This method tests how class GoogleApi reacts when the Google API doesn't respond"""

        def mock_get(*args, **kwargs):
            """Get the mock from MockResponse class"""
            return MockResponse("gpbapp/tests/tests_helpers/google_mock_ko.json")

        monkeypatch.setattr(requests, "get", mock_get)

        # method .get_infos_from_query, which contains requests.get, uses the monkeypatch
        test = GoogleApi('Tour Eiffel')
        assert test.response is False

    def test_no_connection(self, monkeypatch):
        """This method tests how class GoogleApi reacts when the Google API doesn't respond"""

        def mock_get(*args, **kwargs):
            """Get the mock from MockResponse class"""
            return MockResponse("no file")

        monkeypatch.setattr(requests, "get", mock_get)

        # method .get_infos_from_query, which contains requests.get, uses the monkeypatch
        test = GoogleApi('Tour Eiffel')
        assert test.response is False

class TestWikimedia:
    """This class contains tests on WikimediaApi's results"""

    def test_find_page_in_wikipedia(self, monkeypatch):
        """This method tests how class WikimediaApi get datas from Google API requests"""

        def mock_get(*args, **kwargs):
            """Get the mock from MockResponse class"""
            return MockResponse("gpbapp/tests/tests_helpers/wiki_mock_result.json")

        monkeypatch.setattr(requests, "get", mock_get)

        # method .get_infos_from_query, which contains requests.get, uses the monkeypatch
        test = WikimediaApi('Tour Eiffel', "48.85837009999999", "2.2944813")
        assert test.page_id == 1359783
        asserted_content = "La tour Eiffel  est une tour de fer puddlé de "
        asserted_content += "324 mètres de hauteur (avec antennes) "
        asserted_content += "située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars "
        asserted_content += "en bordure de la Seine dans le 7e arrondissement. "
        asserted_content += "Son adresse officielle est 5, avenue Anatole-France."
        assert test.content == asserted_content
        assert test.response

    def test_not_found_in_wikimedia(self, monkeypatch):
        """This method tests how class WikimediaApi reacts when the MediaWiki API doesn't respond"""

        def mock_get(*args, **kwargs):
            """Get the mock from MockResponse class"""
            return MockResponse("gpbapp/tests/tests_helpers/wiki_mock_ko.json")

        monkeypatch.setattr(requests, "get", mock_get)

        test = WikimediaApi("Champs Élysées", "48.8697953", "2.3078204")
        assert test.response is False

    def test_no_connection(self, monkeypatch):
        """This method tests how class GoogleApi reacts when the Google API doesn't respond"""

        def mock_get(*args, **kwargs):
            """Get the mock from MockResponse class"""
            return MockResponse("no file")

        monkeypatch.setattr(requests, "get", mock_get)

        # method .get_infos_from_query, which contains requests.get, uses the monkeypatch
        test = WikimediaApi("Champs Élysées", "48.8697953", "2.3078204")
        assert test.response is False
