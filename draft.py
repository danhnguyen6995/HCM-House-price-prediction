import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
url = "https://rever.vn/mua/can-ho-vinhomes-grand-park-tang-22-view-thanh-pho-thoang-mat"
response = requests.get(url)
source_code = None
if response.status_code == 200:
    source_code=response.text
else: 
    print ("Failed")
soup = BeautifulSoup(source_code,'html.parser')
print(soup)