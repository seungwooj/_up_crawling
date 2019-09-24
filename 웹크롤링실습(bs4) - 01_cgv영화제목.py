
# coding: utf-8

# In[ ]:


# CGV 무비차트 가져오기


# In[1]:


import requests
from bs4 import BeautifulSoup


# In[42]:


r = requests.get("http://www.cgv.co.kr/movies/?ft=0")
c = r.content

#전체 구조 : ol -> li -> div, class:box-content -> strong 안에 영화제목(text)
html = BeautifulSoup(c, "html.parser")

ol = html.find_all("ol")

#try & expect 사용 : 마지막의 strong 안에 text까지 가져온 후 error 방지

try:
    
    for ol in ol:
        li = ol.find_all("li")

        for l in li:
            div = l.find("div",{"class" : "box-contents"})
    
            strong = div.find("strong").text
            print(strong)
        
except:
    print("end")

