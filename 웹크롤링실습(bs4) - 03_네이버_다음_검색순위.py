
# coding: utf-8

# In[1]:


import requests
import time
from bs4 import BeautifulSoup


# ##### 네이버 검색어 순위
# - bs4 사용 : html element를 selector를 사용한다.
# - 네이버 검색어 순위를 가져와 데이터 프레임으로 만들기
# - http://naver.com

# In[2]:


def naver_top20():
    df = pd.DataFrame(columns=["rank","keyword"])
    response = requests.get("http://naver.com")             # response : string
    dom = BeautifulSoup(response.content, "html.parser")    # response를 beautifulsoup을 활용해서 parsing
    keywords = dom.select(".ah_roll .ah_l .ah_item")        # 구조 :  .ah_roll안에 .ah_1 안의 .ah_item (.ah_a 도 됨.)
    for keyword in keywords:
        df.loc[len(df)] = {
            "rank":keyword.select_one(".ah_r").text,
            "keyword":keyword.select_one(".ah_k").text,
        }
    return df


# In[3]:


naver_df = naver_top20()
naver_df


# ##### 다음 검색어 순위

# In[4]:


def daum_top10():
    df = pd.DataFrame(columns=["rank","keyword"])
    response = requests.get("http://daum.net")
    dom = BeautifulSoup(response.content, "html.parser")  #dom선언까지는 동일 (html.parser)
    keywords = dom.select("#mArticle ol.list_hotissue.issue_row.list_mini > li") #select대상이 다름, <li>태그 사용
    for keyword in keywords:
        df.loc[len(df)] = {
            "rank":keyword.select_one(".ir_wa").text.replace("위",""),
            "keyword":keyword.select_one(".link_issue").text,
        }
    return df


# In[5]:


daum_df = daum_top10()
daum_df


# ##### 중복된 키워드 찾아서 출력하기

# In[6]:


result = [keyword for keyword in daum_df["keyword"] if naver_df["keyword"].str.contains(keyword).any() ]
result

