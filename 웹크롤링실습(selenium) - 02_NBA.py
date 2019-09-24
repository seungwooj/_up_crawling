
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd


# In[2]:


driver = webdriver.Chrome()
driver.get('http://stats.nba.com/teams/traditional/?sort=PTS&dir=-1')

teams = driver.find_elements_by_css_selector('.nba-stat-table__overflow>table>tbody>tr')

df = pd.DataFrame(columns=["Position", "Team", "GP", "W", "L", "WIN_P", "MIN", "PTS", "FGM", "FGA", "FG_P",
                          "THREEPM", "THREEPA", "THREEP_P", "FTM", "FTA", "FT%", "OREB", "DREB", "REB", "AST", "TOV",
                          "STL", "BLK", "BLKA", "PF", "PFD", "PLUSMINUS"])

for team in teams:
    Position = team.find_element_by_css_selector('td.rank').text
    Team = team.find_element_by_css_selector('td:nth-child(2)').text
    GP = team.find_element_by_css_selector('td:nth-child(3)').text
    W = team.find_element_by_css_selector('td:nth-child(4)').text
    L = team.find_element_by_css_selector('td:nth-child(5)').text
    WIN_P = team.find_element_by_css_selector('td:nth-child(6)').text
    MIN = team.find_element_by_css_selector('td:nth-child(7)').text
    PTS = team.find_element_by_css_selector('td:nth-child(8)').text
    FGM = team.find_element_by_css_selector('td:nth-child(9)').text
    FGA = team.find_element_by_css_selector('td:nth-child(10)').text
    FG_P = team.find_element_by_css_selector('td:nth-child(11)').text
    THREEPM = team.find_element_by_css_selector('td:nth-child(12)').text
    THREEPA = team.find_element_by_css_selector('td:nth-child(13)').text
    THREEP_P = team.find_element_by_css_selector('td:nth-child(14)').text
    FTM = team.find_element_by_css_selector('td:nth-child(15)').text
    FTA = team.find_element_by_css_selector('td:nth-child(16)').text
    FT_P = team.find_element_by_css_selector('td:nth-child(17)').text
    OREB = team.find_element_by_css_selector('td:nth-child(18)').text
    DREB = team.find_element_by_css_selector('td:nth-child(19)').text
    REB =  team.find_element_by_css_selector('td:nth-child(20)').text
    AST = team.find_element_by_css_selector('td:nth-child(21)').text
    TOV = team.find_element_by_css_selector('td:nth-child(22)').text
    STL = team.find_element_by_css_selector('td:nth-child(23)').text
    BLK = team.find_element_by_css_selector('td:nth-child(24)').text
    BLKA = team.find_element_by_css_selector('td:nth-child(25)').text
    PF = team.find_element_by_css_selector('td:nth-child(26)').text
    PFD = team.find_element_by_css_selector('td:nth-child(27)').text
    PLUSMINUS = team.find_element_by_css_selector('td:nth-child(28)').text
    
    data = {"Position": Position,
            "Team": Team,
            "GP": GP,
            "W": W,
            "L": L,
            "WIN_P": WIN_P,
            "MIN": MIN,
            "PTS": PTS,
            "FGM": FGM,
            "FGA": FGA,
            "FG_P": FG_P,
            "THREEPM": THREEPM,
            "THREEPA": THREEPA,
            "THREEP_P": THREEP_P,
            "FTM": FTM,
            "FTA": FTA,
            "FT_P": FT_P,
            "OREB": OREB,
            "DREB": DREB,
            "REB": REB,
            "AST": AST,
            "TOV": TOV,
            "STL": STL,
            "BLK": BLK,
            "BLKA": BLKA,
            "PF": PF,
            "PFD": PFD,
            "PLUSMINUS": PLUSMINUS}
    
    df.loc[len(df)] = data
        
    driver.close

df


# In[3]:


df.rename(columns={"WIN_P" : "WIN%", "FG_P" : "FG%", "THREEPM" : "3PM", "THREEPA" : "3PA", "THREEP_P" : "3P%",
                   "FT_P" : "FT%", "PLUSMINUS" : "+/-"})

