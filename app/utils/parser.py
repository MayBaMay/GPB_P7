# -*-coding:utf-8-*-

""" This module contains the class Parser"""

import os
import json
import re


class Parser:
    """This class parses user input into usable expression"""

    def __init__(self, query):
        self.query = query
        #parse query
        self.parsed_query = self.parse_query_with_stop_words(self.parse_query_characters)
        after_key_word_list = self.parse_query_with_key_words(self.parsed_query)["after_key_word"]
        self.parsed_after_keyword = self.key_word_string(after_key_word_list)
        before_key_word_list = self.parse_query_with_key_words(self.parsed_query)["before_key_word"]
        self.parsed_before_keyword = self.key_word_string(before_key_word_list)

    @property
    def parse_query_characters(self):
        """parse query's characters to get rid off punctuation"""
        temporary_query = ""
        # parser all characters in query
        for character in self.query.lower():
            # keep only relevant characters
            if re.search("[a-z0-9àâçèéêëîôöùû ]", character):
                temporary_query += character
            # replace - and ' characters
            elif re.search(r"[\'\-]", character):
                temporary_query += " "
        return temporary_query

    @staticmethod
    def load_helping_words(words):
        """Method called to load helping words (stop words and key words)"""
        path = os.path.abspath(os.path.dirname(__file__)) + "/helpers/parsing_helper.json"
        with open(path) as file:
            return json.load(file)[words]

    def parse_query_with_stop_words(self, temporary_query):
        """split query into a list and parse words with stop words"""
        # split the query
        temporary_query = temporary_query.split()
        # load stop words from json file
        stop_words = self.load_helping_words("stop_words")
        # return only words that are not in stop words
        parsed_query = []
        for word in temporary_query:
            if word not in stop_words:
                parsed_query.append(word)
        return parsed_query

    def parse_query_with_key_words(self, temporary_query):
        """Name of the place we are looking for will probably be after
        an adverb, verb or nouns indicating a place
        If such words exists, will try to execute the request to API
        first with words after them and after before them
        If they do not exits, we'll execute request with every word"""
        # load stop words from json file
        key_words = self.load_helping_words("key_words")
        # tcheck if key words exists
        found_key_word = False
        key_word_index = -1 # if not index will be 0
        for word in temporary_query:
            for regex in key_words:
                if re.search(regex, word):
                    found_key_word = True
                    key_word_index = temporary_query.index(word)

        if found_key_word:
            # cut query in two (before and after key word)
            return {"after_key_word" : temporary_query[(key_word_index+1):],
                    "before_key_word" : temporary_query[:(key_word_index)]}
        else:
            # keep all query
            return {"after_key_word" : temporary_query,
                    "before_key_word" : temporary_query}

    @staticmethod
    def key_word_string(query):
        """ return a string of query key words list """
        key_word_string = ""
        for element in query:
            if key_word_string != "":
                key_word_string += " " + element
            else:
                key_word_string += element
        return key_word_string
