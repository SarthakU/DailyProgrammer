## Match String on Web Page
##
## challenge #17 (intermediate)
## https://redd.it/qhe4u
##
##
## sarthak7u@gmail.com

import requests

def match_string(url, string):
    data = requests.get(url)
    return data.text.count(string)

