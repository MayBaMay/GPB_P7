# -*-coding:utf-8-*-
"""This module contains a class generating GrandPy's answer"""

import os
import json
from random import randint


class GrandPy:
    """This class generate random answers for each step of the response"""

    def __init__(self):
        self.presentation = self.random_answers("presentation")
        self.geo_answer = self.random_answers("geo_answers")
        self.wiki_answer = self.random_answers("wiki_answers")
        self.geo_noresults_answer = self.random_answers("geo_noresults_answer")
        self.wiki_noresults_answer = self.random_answers("wiki_noresults_answer")

    @staticmethod
    def load_sentences(answer_type):
        """this method loads all sentences grandPy could use from the file gdpy_sentences.json"""
        path = os.path.abspath(os.path.dirname(__file__)) + "/helpers/gdpy_sentences.json"
        with open(path) as file:
            return json.load(file)[answer_type]

    def random_answers(self, answer_type):
        """this method returns a random sentense concidering the type of sentence expected"""
        answers_list = self.load_sentences(answer_type)
        return answers_list[randint(0, len(answers_list)-1)]
