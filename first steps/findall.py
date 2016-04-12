from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.tayara.tn/gafsa/multimedia-à_vendre")
bsObj= BeautifulSoup(html)
titres=bsObj.findAll("a",{"class","history"})
for titre in titres
	print (titre.get_text())