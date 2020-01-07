"""This module contains the class GoogleApi"""

import requests
from gpbapp import app


class GoogleApi:
    """This class gets infos from google maps API"""

    def __init__(self, query):
        self.query = query
        self.key = app.config['GOOGLE_GEO_KEY']
        self.response = False
        self.infos = {"address" : "", "lat" : 0, "lng" : 0}
        self.query_datas = self.get_datas_from_api()
        self.get_infos_from_datas()


    def get_datas_from_api(self):
        """this method requests an url research to google API
        parameters provided are formatted_address,name,geometry,place_id
        then loading it with json and get needed informations from json """
        try:
            # https://developers.google.com/places/web-service/search
            search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
            # https://2.python-requests.org/en/master/user/quickstart/#make-a-request
            search_payload = {"key": self.key,
                              "input":self.query,
                              "inputtype":"textquery",
                              "fields":"formatted_address,name,geometry,place_id"}
            search_result_requests = requests.get(search_url, params=search_payload)
            return search_result_requests.json()
        except:
            datas = {"status": "NO CONNECTION"}
            return datas


    def get_infos_from_datas(self):
        """this method get infos from datas"""
        if self.query_datas["status"] == "OK":
            self.response = True
            self.infos["address"] = self.query_datas["candidates"][0]["formatted_address"]
            self.infos["lat"] = self.query_datas["candidates"][0]["geometry"]["location"]["lat"]
            self.infos["lng"] = self.query_datas["candidates"][0]["geometry"]["location"]["lng"]
