
# coding: utf-8

# In[7]:


import requests
import time
from bs4 import BeautifulSoup


# ##### 네이버 주식 데이터 가져오기
# - api 사용 : json 파싱을 한다.
# - 네이버 주식 페이지에서 주식 데이터를 가져와 데이터 프레임으로 만들기
# - http://m.stock.naver.com
# 
# <순서><br>
# 1. make_url : 주식 데이터를 가져올 페이지에서 개발자도구 - XHR - Headers에서 url따오기 (pagesize, page는 함수의 인수로 넣어준다.)
# 2. get_data : url을 한번 클릭해보면 전체 json형식이 나옴 (XHR - Preview에서 구조 파악 가능)
# - response : request로 url을 string으로 받아옴
# - json_info : response에서 string을 json형태로 변경
# - 이후 json의 구조를 파악해서 원하는 정보가 있는 json을 인수로 지정, dataframe만들기

# In[8]:


def make_url(pageSize=10, page=1):
    return "http://m.stock.naver.com/api/json/sise/siseListJson.nhn?menu=market_sum&sosok=0&pageSize=" + str(pageSize) + "&page=" + str(page)

  
def get_data(url):
    response = requests.get(url)
    json_info = response.json()   # <- url을 string -> json형태로 변경해서 날림
    companys = json_info["result"]["itemList"]
    df = pd.DataFrame(columns=["종목", "시세", "전일비", "등락율", "시가총액", "거래량"])
    for company in companys:
        df.loc[len(df)] = {
            "종목":company["nm"],
            "시세":company["nv"],
            "전일비":company["cv"],
            "등락율":company["cr"],
            "시가총액":company["mks"],
            "거래량":company["aq"],
        }
    return df


# In[9]:


url = make_url(100,1)
df = get_data(url)
print(df.shape)
df.tail()


# ##### Dark Sky API
# - 날씨 정보를 알려주는 api
# - https://darksky.net/dev
# - pip3 install python-forecastio
# 
# 
# <순서><br>
# 1. token입력 : 개인메일로 로그인시 생성되는 token 함수에 입력
# 2. api documentation : format함수로 위도, 경도를 넣어줌. - https://api.darksky.net/forecast/[key]/[latitude],[longitude]
# 3. 이후 response / json_info 통해서 url -> string -> json으로 저장
# 4. json의 형식 에 맞게 정보 입력

# In[4]:


import forecastio
FORECAST_TOKEN = "aa20c11702caa31ef820aaba4a1f533b" #개인 메일로 로그인하면 token생성


# In[5]:


def forecast(lat,lng):
    url = "https://api.darksky.net/forecast/{}/{},{}".format(FORECAST_TOKEN, lat, lng)
    response = requests.get(url)
    json_info = response.json()
    return json_info["hourly"]["summary"] #currently, minutely, hourly, daily, alerts, flags


# In[6]:


lat = 37.8267
lng = 122.4233
forecast(lat,lng)

