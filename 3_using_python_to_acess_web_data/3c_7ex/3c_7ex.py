import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
l = []
url = input('Enter - ')
count = int(input("counts:"))
pos = int(input("position:"))
for i in range(0,count):
    html = urllib.request.urlopen(url , context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    pos1 = tags[pos-1].get('href',None).find('_')
    s = tags[pos-1].get('href',None)[pos1+4:]
    pos2 = s.find('.')
    s = s[:pos2]
    l.append(s)
    url = tags[pos-1].get('href',None)
print(l[count-1])
