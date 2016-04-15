# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
address = "http://www.tayara.tn/gafsa/multimedia-à_vendre"
addressParts = address.replace("http://", "").split("/")
#only print the first string
#result will be 3 strings cause it split the hole url into strings when there is a /
print (addressParts[0])
#we can use it as a funtion
#def splitAddress(address):
#    addressParts = address.replace("http://", "").split("/")
#    return addressParts
