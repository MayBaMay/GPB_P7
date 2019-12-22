#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module tests methods of the parsing class"""

from ..utils.parser import Parser

QUERY_ALL = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? "
QUERY_ALL += "Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le "
QUERY_ALL += "musée d'art et d'histoire de Fribourg, s'il te plaît?"
QUERY_PUNCTUATION_OUT = "salut grandpy comment s est passé ta soirée avec grandma "
QUERY_PUNCTUATION_OUT += "hier soir au fait pendant que j y pense pourrais tu m indiquer "
QUERY_PUNCTUATION_OUT += "où se trouve le musée d art et d histoire de fribourg s il te plaît"
QUERY_STOP_WORDS_OUT = ['salut', 'soirée', 'soir', 'indiquer', 'trouve', 'musée',
                        'art', 'histoire', 'fribourg']
QUERY_AFTER_KEY_WORD = ['musée', 'art', 'histoire', 'fribourg']
QUERY_BEFORE_KEY_WORD = ['salut', 'soirée', 'soir', 'indiquer']


def test_take_out_punctuation():
    """tests take out punctuation from query"""
    parser = Parser(QUERY_ALL)
    punctuation_out = parser.parse_query_characters
    assert punctuation_out == QUERY_PUNCTUATION_OUT

def test_take_out_stopwords():
    """tests split query and take out stop key_words"""
    parser = Parser(QUERY_ALL)
    stop_word_out = parser.parse_query_with_stop_words(QUERY_PUNCTUATION_OUT)
    assert stop_word_out == QUERY_STOP_WORDS_OUT

def test_after_key_word():
    """tests search keyword and return what is after"""
    parser = Parser(QUERY_ALL)
    after_key_word = parser.parse_query_with_key_words(QUERY_STOP_WORDS_OUT)["after_key_word"]
    assert after_key_word == QUERY_AFTER_KEY_WORD

def test_before_key_word():
    """tests search keyword and return what is before"""
    parser = Parser(QUERY_ALL)
    before_key_word = parser.parse_query_with_key_words(QUERY_STOP_WORDS_OUT)["before_key_word"]
    assert before_key_word == QUERY_BEFORE_KEY_WORD

def test_no_key_word():
    """tests if query has no key words in it"""
    query = "Musée d'art et d'histoire de Fribourg, s'il te plaît?"
    parser = Parser(query)
    without_key_word = parser.parse_query_with_key_words(['musée', 'art', 'histoire', 'fribourg'])
    assert without_key_word["after_key_word"] == ['musée', 'art', 'histoire', 'fribourg']
    assert without_key_word["before_key_word"] == ['musée', 'art', 'histoire', 'fribourg']

def test_result_is_string():
    """tests if the result is a string"""
    parser = Parser(QUERY_ALL)
    result = parser.key_word_string(QUERY_AFTER_KEY_WORD)
    assert isinstance(result, str)
