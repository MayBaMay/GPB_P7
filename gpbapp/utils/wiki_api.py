# -*-coding:utf-8-*-

"""This module contains the class WikimediaApi"""

import requests

class WikimediaApi:
    """This class gets infos from mediawiki API"""

    def __init__(self, key_words, lat, lng):
        self.key_words = key_words
        self.lat = lat
        self.lng = lng
        self.url = "https://fr.wikipedia.org/w/api.php"
        self.page_id = 0
        self.response = self.find_wiki()

    def find_wiki(self):
        """This method calls find_with_coordinates method doing a request to the APi
        with the coordinates, and if it fails, it calls a method using the parsed query
        If one of those method succeed, it calls an other methor requesting an extract
        with the page_id founded.
        It returns True (API request succeed) or False (API request failed)"""
        if self.find_with_coordinates():
            self.content = self.find_extract_with_page_id()
            return True

        if self.find_with_query():
            self.content = self.find_extract_with_page_id()
            return True

        return False


    def request_api(self, params):
        """Method calling the request.get method and returning it in a json format"""
        try:
            response = requests.get(url=self.url, params=params)
            return response.json()
        except requests.exceptions.RequestException:
            return 'error'

    def find_with_coordinates(self):
        """This method requests a geosearch of coordinates in MediaWiki API"""
        # https://www.mediawiki.org/wiki/API:Geosearch
        params = {
            "action": "query",
            "format": "json",
            "list":"geosearch",
            "gsradius" : "5000",
            "gslimit" : "1",
            "gscoord" : "{}|{}".format(self.lat, self.lng)
        }
        wiki_datas = self.request_api(params)
        if 'error' in wiki_datas:
            # returns 'error' if the request fails
            return False
        # change attribute self.page_id value if it succeed
        self.page_id = wiki_datas["query"]["geosearch"][0]["pageid"]
        return True

    def find_with_query(self):
        """This method requests a research of the query in MediaWiki API"""
        params = {
            "action": "query",
            "format": "json",
            "list":"search",
            "srsearch": self.key_words
        }
        wiki_datas = self.request_api(params)
        if 'error' in wiki_datas:
            # returns 'error' if the request fails
            return False
        # change attribute self.page_id value if it succeed
        self.page_id = wiki_datas["query"]["search"][0]["pageid"]
        return True

    def find_extract_with_page_id(self):
        """With the page_id this method get an extract of the wikipedia page"""
        # https://www.mediawiki.org/wiki/Template:Api_help/fr
        params = {
            "format": "json",
            "action": "query",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "exsentences": "2",
            "pageids" : self.page_id
        }
        wiki_datas = self.request_api(params)
        return wiki_datas["query"]["pages"][str(self.page_id)]["extract"]
