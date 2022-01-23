import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

#ignor SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#if we didn't write this things here the https won't work


url = input("Enter -")
html = urllib.request.urlopen(url , context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
#this return a list of tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
