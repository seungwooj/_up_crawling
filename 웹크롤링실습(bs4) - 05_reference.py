
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import konlpy
from konlpy.tag import Twitter
import pandas as pd
from collections import Counter


# In[2]:


#konlpy 패키지 사용을 위한 객체 선언
twitter = Twitter()


# In[3]:


#전체 데이터 갯수를 가져오는 함수 
def get_total(keyword) :
    url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%" + keyword +      "&search.menuid=&search.searchBy=1&search.sortBy=date&search.clubid=10258021&search.option=0&search.defaultValue="
    response = requests.get(url)
    dom = BeautifulSoup(response.content, "html.parser")
    return dom.select_one("#ct > div.search_contents > div.search_sort > div.sort_l > span").text


# In[4]:


#해당 키워드와 페이지 리스트를 가져오는 함수
def get_list(keyword, page) : 
    url = "https://m.cafe.naver.com/ArticleSearchListAjax.nhn?search.query=" + keyword +     "&search.menuid=&search.searchBy=0&search.sortBy=date&search.clubid=10258021&search.option=0&search.defaultValue=&search.page=" +     str(page)
    response = requests.get(url)
    dom = BeautifulSoup(response.content, "html.parser")
    return dom.select("a")

dom = get_list("여행", 1)


# In[5]:


def get_link(dom) : 
    ls = []
    for i in range(0, len(dom)) :
        link = dom[i].get('href')
        if len(link) > 2 and "Comment" not in link and "javascript" not in link :
            link = "http://m.cafe.naver.com"+link
            ls.append(link)
    return ls


# In[6]:


get_link(dom)


# In[7]:


#페이지 들어가서 텍스트 데이터 긁어오는 함수
def get_text(link) :
    headers = {
        "Referer"  : "https://m.cafe.naver.com/ArticleRead.nhn?clubid=10258021&menuid=251&articleid="+ \
        "15027772&query=%ED%8E%AB%EC%8B%9C%ED%84%B0",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }
    
    response = requests.get(link, headers = headers)
    dom = BeautifulSoup(response.content, "html.parser")
    text = dom.select_one("#postContent").text
    return text


# In[8]:


def get_all_texts(keyword) :
    total = get_total(keyword)
    pages = int(total) // 20 + 1
    text_sets = []
    for page in range(1, pages + 1) :
        text = get_list(keyword, page)
        link_ls = get_link(text)
        for link in link_ls :
            all_text = get_text(link)
            all_text = twitter.nouns(all_text)
            text_sets.extend(all_text)
    return text_sets


# In[ ]:


text_ls = get_all_texts("여행")


# In[ ]:


Counter(text_ls).most_common(50)

