#Crawl data
import requests
import pandas as pd
import numpy as np
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
for i in range(1, 3): 
    url_i =url +str(i)
    response = requests.get(url_i)
    source_code = None
    if response.status_code == 200:
        source_code=response.text
    else: 
        print ("Failed")
        continue
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(source_code,'html.parser')
    elements_w_class=soup.find_all(class_="listing-address")
    for element in elements_w_class:
        housecode=element.find_all('p')[0].text.strip().split(' ')[0]
        province = element.find_all('a')[-1].text.strip().split(',')[0]
        if element.find_all('a')[-2].text.strip().split(',')[0] != province:
            district=element.find_all('a')[-2].text.strip().split(',')[0]
        else: None
        if element.find_all('a')[-3].text.strip().split(',')[0] != district:
            ward=element.find_all('a')[-3].text.strip().split(',')[0]
        else: None
        if element.find_all('a')[0].text.strip().split(',')[0] != ward:
            street=element.find_all('a')[0].text.strip().split(',')[0]
        else: None
        
        element_w_info_class = element.find_next('ul',class_="listing-info")
        if 'suite' in str(element_w_info_class.find_all('li')[0]):
            bedroom=element_w_info_class.find_all('li')[0].text.strip()
        else: bedroom='NA'
        if 'bath' in str(element_w_info_class.find_all('li')[1]):
            bathroom=element_w_info_class.find_all('li')[1].text.strip()
        else: bathroom='NA'
        if element_w_info_class.find_all('li')[2].text.strip().split(' ')[0] != bathroom:
            square=element_w_info_class.find_all('li')[2].text.strip().split(' ')[0]
        else:square='NA'
        if element_w_info_class.find_all('li')[-1].text.strip()==element_w_info_class.find_all('li')[2].text.strip():
            compass='NA'
        else: compass=element_w_info_class.find_all('li')[-1].text.strip()
        
        element_w_action_class = element.find_next('div',class_="listing-price")
        price= element_w_action_class.text.strip().split(' ')[0]
        #print(housecode,street,ward,district,square,compassing)
        bds_data.append({
        'Housecode': housecode,
        'Street': street,
        'Ward': ward,
        'District': district,
        'Bedroom': bedroom,
        'Bathroom': bathroom,
        'Square (m2)': square,
        'Compass': compass,
        'Price (Bil. VND)': price
        })
df = pd.DataFrame(bds_data)
print(df.head())

#Remove duplicate 
df_nodup=df.drop_duplicates(subset=['Housecode'],keep=False)
df_nodup.to_csv('bds_data4.csv', index=False, encoding='utf-8-sig')