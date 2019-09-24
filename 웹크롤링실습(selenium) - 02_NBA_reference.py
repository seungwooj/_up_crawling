
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver


# In[2]:


driver = webdriver.Chrome("../../DataScience/driver/chromedriver")


# In[3]:


driver.get("http://stats.nba.com/teams/traditional/?sort=PTS&dir=-1&Season=2017-18&SeasonType=Regular%20Season")


# In[4]:


df = pd.DataFrame(columns=['Rank','TEAM','GP','W','L','WIN%','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','TOV','STL','BLK','BLKA','PF','PFD','+/-'])


# In[5]:


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

nba_stat_area = soup.find('div','nba-stat-table')
team_info = nba_stat_area.find('tbody').find_all('tr')

# team 은 30개의 팀을 선택
for team in range(30):
    tmp_team = []   # 임시 리스트를 생성
    # team의 stat column이 28개 이므로 팀당 28개의 컬럼의 stat_value를 for문을
    # 돌려서 tmp_team 리스트에 저장
    for col in range(28):
        tmp_value = team_info[team].find_all('td')[col].get_text()
        tmp_team.append(tmp_value)
    # 저장된 tmp_team 리스트의 값들을 df 데이터프레임에 넣어준다.
    df.loc[team] = tmp_team


# # Column Discription
# 
# - `GP` : game played
# - `MIN` : minutes
# - `PTS` : points
# - `FGM` : field goals made
# - `FGA` : field goals attempted
# - `FG%` : field goals percentage
# - `3PM` : 3point goals made
# - `3PA` : 3point goals attempted
# - `3P%` : 3point goals percentage
# - `FTM` : free throws made
# - `FTA` : free throws attempted
# - `FT%` : free throws percentage
# - `OREB` : offensive rebounds
# - `DREB` : defensive rebounds
# - `REB` : rebounds
# - `AST` : assists
# - `TOV` : turnovers
# - `STL` : steals
# - `BLK` : blocks
# - `BLKA` : bolcked field goal attempts
# - `PF` : personal foul
# - `PFD` : personal foul drawn
# - `+/-` : the point differential when a player or team is on the floor

# In[6]:


df


# In[7]:


df.to_csv('../data/NBA_Team_stats.csv', sep = ',')

