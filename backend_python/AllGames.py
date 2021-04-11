from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

Name = "qxt"

hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}

def parseOPGG(Name):

    url = 'https://www.op.gg/summoner/userName=' + Name

    driver = webdriver.Chrome('chromedriver.exe')
    
    driver.get(url)

    ## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
    driver.implicitly_wait(3)
    
    resp = driver.page_source
    

    xpath = """//*[@id="SummonerRefreshButton"]"""

    driver.find_element_by_xpath(xpath).click() # 최근전적으로 갱신하기
    time.sleep(10)

    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[4]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[5]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[6]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[7]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break 
        except:
            continue

    time.sleep(5)

    page = driver.page_source
    
    soup = BeautifulSoup(page, 'html.parser')

    game_time = []

    # 게임 시간
    all_games_rows = soup.find_all('div', class_='GameItemWrap')

    for all_games_row in all_games_rows:
        game_time_content = all_games_row.find('div', class_='Content')

        game_time_gamestats = game_time_content.find('div', class_='GameStats')

        game_time_timestamp = game_time_gamestats.find('div', class_='TimeStamp')

        game_times = game_time_timestamp.find('span', class_='_timeago _timeCountAssigned tip').get('title')

        game_time.append(game_times)

        # print(game_times)
    print(len(game_time))


# 소환사 이름 입력
if __name__ == "__main__":
    
    parseOPGG("hide on bush")
