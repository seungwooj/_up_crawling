
# coding: utf-8

# In[2]:


import requests
from scrapy.http import TextResponse


# In[3]:


# 웹 페이지에 연결
req = requests.get('https://search.shopping.naver.com/search/all.nhn?query=%EB%B2%A0%EA%B0%9C&cat_id=&frm=NVSHATC')

# response 객체 생성
response = TextResponse(req.url, body=req.text, encoding='utf-8')

