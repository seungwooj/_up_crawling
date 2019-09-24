
# coding: utf-8

# ##### 네이버 중고나라 크롤링
# - http://cafe.naver.com/joonggonara
# - 중고나라 검색 키워드를 입력받아 판매중인 상품에 대한 제목, 링크, 조회수, 등록날짜, 가격을 크롤링하여 데이터 프레임 만들기
# - 모바일 페이지를 활용하세요
# 
# 
# - get_total : 전체 데이터 갯수를 가져오는 함수
# - get_items : 아이템 리스트를 가져오는 함수
# - get_price : 상세 페이지에서 가격정보를 가져오는 함수
# - make_datas : 아이템을 데이터 리스트로 만드는 함수 (판매 중인 데이터만)
# - all_datas : 키워드를 입력받아 전체 데이터를 가져오는 함수

# In[1]:


import requests
import pandas as pd 
from bs4 import BeautifulSoup


# In[2]:


# 전체 데이터 갯수를 가져오는 함수
def get_total(keyword):
    pass

# 테스트 코드
get_total("트레이더스 에어프라이어")


# In[3]:


# 아이템 리스트를 가져오는 함수
def get_items(keyword, page):
    pass

# 테스트 코드
items = get_items("트레이더스 에어프라이어", 1)    
len(items)


# In[4]:


# 상세 페이지에서 가격정보를 가져오는 함수
def get_price(link):
    pass
    
# 테스트 코드
link = "https://m.cafe.naver.com/ArticleRead.nhn?clubid=10050146&menuid=451&articleid=455147331&query=%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8D%94%EC%8A%A4+%EC%97%90%EC%96%B4%ED%94%84%EB%9D%BC%EC%9D%B4%EC%96%B4"
get_price(link)


# In[5]:


# 아이템을 데이터 리스트로 만드는 함수
def make_datas(items):
    pass

# 테스트 코드
datas = make_datas(items)
len(datas)


# In[6]:


# 키워드를 입력받아 전체 데이터를 가져오는 함수
def all_datas(keyword):
    pass
    
# 테스트 코드
datas = all_datas("트레이더스 에어프라이어")
len(datas)


# In[7]:


# 데이터 프레임을 만드는 코드
datas = all_datas("트레이더스 에어프라이어")

columns = ["title", "link", "views", "date", "price"]
df = pd.DataFrame(datas, columns=columns)
df

