#!/usr/bin/env python3
import pystache
#import subprocess
import os
import requests
import datetime
from pytz import reference

def myip():
    #"curl -s -w '\n' ident.me"
    return requests.get("http://ident.me").text

def timestamp():
    tz = reference.LocalTimezone().tzname(datetime.datetime.now())
    return datetime.datetime.now().strftime("%A %B %d, %Y %H:%M:%S ") + tz

#print(myip())

#print(timestamp())

def render(template, data):
    return pystache.render(template, data)

file = open(os.path.join(os.path.dirname(__file__),'templates/general.html'))

text = file.read()


data = {
    'timestamp': timestamp(),
    'title': "[Isaac's Harbour] PI Ping"
}

print(render(text, data))
