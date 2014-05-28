'''
This script will parse apart a chat string input into
mentions, links, and emoticons
'''

import argparse
import json
import re
from urllib2 import Request, urlopen

def parse_chat(message):
    '''
    Takes a message string and outputs json of
    mentions, links, and emoticons
    '''
    output = {}

    mentions = re.findall(r"(?:^|\s)@(\w+)", message)
    if mentions:
        output["mentions"] = mentions

    emoticons = re.findall(r"(?:^|\s)\(([^)]{0,15})\)", message)
    if emoticons:
        output["emoticons"] = emoticons

    links = re.findall(r"(https?://\S+)", message)
    if links:
        links_array = []
        for link in links:
            url = link
            title = get_title(link)
            links_array.append({"url": url, "title": title})
        output["links"] = links_array

    return json.dumps(output)

def get_title(href):
    '''Makes an http request to input and returns the page's title'''
    source = urlopen(Request(href)).read()
    title = re.search(r"<title>(.*?)</title>", source).group(1)
    return title

def parse_args():
    '''Defines command line arguments and parses them into variables'''

    parser = argparse.ArgumentParser(
        description="Parses chat into relevant metadata")

    parser.add_argument('chat', help="Chat String (ex. '@brian sup dog?')")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    ARGS = parse_args()
    parse_chat(ARGS.chat)
