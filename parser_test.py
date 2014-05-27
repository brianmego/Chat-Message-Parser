import sys
import os
from nose.tools import istest
import chat_parser

@istest
def parseChat_HasMention_JSONWithMention():
    chat = "@chris you around?"
    expected = """{"mentions": ["chris"]}"""
    actual = chat_parser.parse_chat(chat)
    print actual
    print expected
    assert expected == actual

@istest
def parseChat_HasEmoticons_JSONWithEmoticons():
    chat = "Good morning! (megusta) (coffee)"
    expected = """{"emoticons": ["megusta", "coffee"]}"""
    actual = chat_parser.parse_chat(chat)
    print actual
    print expected
    assert expected == actual

@istest
def parseChat_HasLink_JSONWithLink():
    chat = "Olympics are starting soon; http://www.nbcolympics.com"
    expected = """{"links": [{"url": "http://www.nbcolympics.com", "title": "| NBC Olympics"}]}"""
    actual = chat_parser.parse_chat(chat)
    print actual
    print expected
    assert expected == actual

@istest
def parseChase_HasMultipleLinks_JSONWithLinks():
    chat = "http://www.nbcolympics.com http://www.google.com"
    expected = """{"links": [{"url": "http://www.nbcolympics.com", "title": "| NBC Olympics"}, {"url": "http://www.google.com", "title": "Google"}]}"""
    actual = chat_parser.parse_chat(chat)
    print actual
    print expected
    assert expected == actual

@istest
def parseChat_HasMentionsAndEmoticonAndLinks_JSONWithMentionsAndEmoticonAndLinks():
    chat = "@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016"
    expected = """{"mentions": ["bob", "john"], "emoticons": ["success"], "links": [{"url": "https://twitter.com/jdorfman/status/430511497475670016", "title": "Twitter / jdorfman: nice @littlebigdetail from ..."}]}"""
    actual = chat_parser.parse_chat(chat)
    print actual
    print expected
    assert expected == actual

