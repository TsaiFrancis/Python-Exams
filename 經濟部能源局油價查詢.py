#!/usr/bin/env python
# coding: utf-8

# In[107]:


import pandas as pd
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://www2.moeaboe.gov.tw/oil102/oil2017/newmain.asp'
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

def world_oil():
    w_oils = soup.find('div',{'class','landingbox-Wideshell-RightInner'}).find_all('div',{'class','font-number'})
    print('⦿最新國際原油價格\n')
    W_Price = []
    for w_oil in w_oils:
        W_price = w_oil.text.strip()
        W_Price.append(W_price)
    df_world = pd.DataFrame({'原油':['West Texas','North Sea Brandt','Dubai'],
                             '價格(美元/桶)':W_Price})
    print(df_world)
    
def domestic_oil():
    d_oils = soup.find('div',{'class','landingbox-NarrowInnerBox_list landingbox-font'}).find_all('span',{'class','font-number'})
    print('⦿最新油品公告參考零售價格(中油)\n')
    D_Price = []
    for d_oil in d_oils[:4]:
        D_price = d_oil.text.strip()
        D_Price.append(D_price)
    df_domestic = pd.DataFrame({'種類':['92 Unleaded Gasoline','95 Unleaded Gasoline','98 Unleaded Gasoline','Super Diesel'],
                                '價格(元/桶)':D_Price})
    print(df_domestic)
    
world_oil()
print()
domestic_oil()


# In[ ]:




