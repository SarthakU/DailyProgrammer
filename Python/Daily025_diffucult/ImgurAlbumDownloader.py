## IMGUR ALBUM DOWNLOADER
##
## challenge #36 (difficult)
## http://www.reddit.com/r/dailyprogrammer/comments/qzig1/3162012_challenge_26_difficult/
##
##
## sarthak7u@gmail.com
##

import urllib2
import urllib

album = raw_input("Enter you album URL : ")
if album[:8] != 'https://':
    album = 'https://' + album
response = urllib2.urlopen(album)
html = response.read()
links = []
index = 0

for i in html:
    if html[index:index+12] == "i.imgur.com/" :
        link = 'https://i.imgur.com/'
        index+=12
        while html[index] != '"':
            link += html[index]
            index +=1
        # checks whether repeatative link or redirecting link
        if links.count(link) == 0 and link.count("?") == 0:
            # checks whether thumbnail by checking whether last character s
            if link[-5:-6:-1] != "s":
                links.append(link)
    index += 1
index = 1

for i in links:
    open("a.jpg",'w').close()
    print "Downloading -->", links[index - 1]
    urllib.urlretrieve(links[index - 1],"%04d.jpg" % index)
    index += 1
