#!/usr/bin/env python
# coding: utf-8

# In[35]:


import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://www.ettoday.net/news/focus/%E5%9C%8B%E9%9A%9B/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

def world_hotspot():
    news_hss = soup.find('div',{'class':'part_list_3'}).find_all('a')
    print('⦿國際焦點\n')
    for news_hs in news_hss:
        print('標題:',news_hs.get_text())
        print('連結: https://www.ettoday.net%sl\n' %news_hs['href'])
        
def world_hot():
    news_hs = soup.find('div',{'class':'two_col clearfix'}).find_all('a')
    print('⦿國際熱門\n')
    for news_h in news_hs:
        print('標題:',news_h.get_text())
        print('連結: https://www.ettoday.net%s\n' %news_h['href'])
        
world_hotspot()
print()
world_hot()


# In[ ]:




