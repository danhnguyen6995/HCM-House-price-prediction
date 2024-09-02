#Crawl data
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
bds_data=[]
url = 'https://rever.vn/s/ho-chi-minh/mua/can-ho?page='
ward=None
district=None
street=None
province=None
bedroom=None
bathroom=None
square=None
compass=None
for i in range(1, 2): 
    url_i =url +str(i)
    response = requests.get(url_i)
    source_code = None
    if response.status_code == 200:
        source_code=response.text
    else: 
        print ("Failed")
        continue
    soup = BeautifulSoup(source_code,'html.parser')
    elements_w_class=soup.find_all(class_="listing-price-link")
    for link in elements_w_class:
        href=link.get('href')
        full_url=[]
        full_url=requests.compat.urljoin(url,href).split("\n")
        print(full_url)
        # for sub_link in full_url: 
        #     response2 = requests.get(sub_link)
        #     sub_source_code = None
        #     if response2.status_code == 200:
        #         sub_source_code=response2.text
        #     else: 
        #         print ("Failed")
        #         continue
        #     sub_soup = BeautifulSoup(sub_source_code,'html.parser')
        #     print (sub_soup)