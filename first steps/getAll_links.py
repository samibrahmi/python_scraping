from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
html = urlopen("http://www.tayara.tn/")
bsObj = BeautifulSoup(html)
startTime = time.time()
for link in bsObj.findAll("a"):
	if 'href' in link.attrs:
		print(link.attrs['href'])
print (time.time() - startTime)