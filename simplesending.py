import pystache
#import subprocess
import requests
import datetime
from pytz import reference

def myip():
    #"curl -s -w '\n' ident.me"
    return requests.get("http://ident.me").text

def timestamp():
    tz = reference.LocalTimezone().tzname(datetime.datetime.now())
    return datetime.datetime.now().strftime("%A %B %d, %Y %H:%M:%S ") + tz

print(myip())

print(timestamp())

print(pystache.render('<div><b>Timestamp:</b> {{timestamp}}</div>', {'timestamp': timestamp()}))
