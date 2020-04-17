#!/usr/bin/env python
# coding: utf-8

# In[28]:


#第1題
import re

def reserve(f_list,start,end):
    while start <= end:
        f_list[start],f_list[end ]= f_list[end],f_list[start]
        end -= 1
        start += 1

f = input('please enter a sentence:')
f_list = list(f)

i = 0
while i < len(f_list):
    if f_list[i] != ' ':
        start = i
        end = start + 1
        while (end < len(f_list)) and (f_list[end]!=' '):
            end += 1
        if end - start > 1:
            reserve(f_list, start, end - 1)
            i = end
        else:
            i = end
    else:
        i += 1

s = ''.join(f_list)
print(s)


# In[12]:


#第2題
num = int(input('input: '))
numlist = list(range(1,num + 1))

for i in range(1,num + 1):
    if i%15 != 0:
        if (i%3 == 0) or (i%5 == 0):
            numlist.remove(i)

print('output:',len(numlist))


# In[ ]:


#第3題

#因為三個袋子標籤都是標錯的，所以先從"混和袋"開始摸，如果摸出的是鉛筆，那就表示這一袋裝的全都是鉛筆
#剩下的袋子分別為"原子筆袋"和"鉛筆袋"，以及兩種結果分別為原子筆及混和
#由此可知"鉛筆袋"裝的都是原子筆，而"原子筆袋"裡裝的是混和的筆


# In[ ]:


#第4題

#一杯冰雪奇緣原本要價900元，但因為服務生鬼迷心竅，讓遊客誤以為一杯是810元(服務生退給遊客90元)
#其實遊客只要付750元而已，因為服務生私吞的60元是遊客多付的錢，所以810-60=750元才是合理的解釋
#服務生的私吞是對於遊客上的損失，而對餐廳收入並沒有影響(餐廳本來就是要收一杯750元)

