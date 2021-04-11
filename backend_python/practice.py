from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import time
import itertools
import folium
from collections import Counter
from folium.plugins import HeatMap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

Name = "qxt"

hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}

def set_config():
    # 폰트, 그래프 색상 설정
    font_list = fm.findSystemFonts(fontpaths=None, fontext="ttf")
    if any(["notosanscjk" in font.lower() for font in font_list]):
        plt.rcParams["font.family"] = "Noto Sans CJK JP"
    else:
        if not any(["malgun" in font.lower() for font in font_list]):
            raise Exception(
                "Font missing, please install Noto Sans CJK or Malgun Gothic. If you're using ubuntu, try `sudo apt install fonts-noto-cjk`"
            )

        plt.rcParams["font.family"] = "Malgun Gothic"

    sns.set_palette(sns.color_palette("Spectral"))
    plt.rc("xtick", labelsize=6)


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
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[8]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[9]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[10]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[11]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[12]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[13]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[14]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[15]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[16]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[17]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[18]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[19]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[20]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[21]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[22]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[23]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[24]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[25]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[26]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[27]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[28]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[29]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[30]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[31]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[32]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[33]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[34]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[35]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[36]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[37]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[38]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[39]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[40]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[41]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[42]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[43]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[44]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[45]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[46]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[47]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[48]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[49]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[50]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[51]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    while True:
        try:
            xpath = """//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[52]/a"""
            driver.find_element_by_xpath(xpath).click() # 전적 추가로 보기 버튼 누르기
            break
        except:
            continue
    
   
    time.sleep(5)

    page = driver.page_source
    
    soup = BeautifulSoup(page, 'html.parser')

    game_time = []

    # 게임 시간 리스트 초기화
    game_times_list = []
    # 게임 시간 기준대로 나누는거 초기화
    game_times_split_day = []
    game_times_split_month = []
    game_times_split_year = []
    result = []
    # 년월일 담을 배열
    year = []
    month = []
    day = []
    # 요일 세기
    monday = 0
    tuesday = 0
    wednesday = 0
    thursday = 0
    friday = 0
    saturday = 0
    sunday = 0


    # 게임 시간
    all_games_rows = soup.find_all('div', class_='GameItemWrap')

    for all_games_row in all_games_rows:
        game_time_content = all_games_row.find('div', class_='Content')

        game_time_gamestats = game_time_content.find('div', class_='GameStats')

        game_time_timestamp = game_time_gamestats.find('div', class_='TimeStamp')

        game_times = game_time_timestamp.find('span', class_='_timeago _timeCountAssigned tip').get('title')

        # 년도 자르기
        game_times_split_year = game_times.split('년')
        game_times_split_year = game_times_split_year[0]
        year.append(game_times_split_year)

        # 월 자르기
        game_times_split_month = game_times.split('년 ')
        game_times_split_month = game_times_split_month[1].split('월')
        game_times_split_month = game_times_split_month[0]
        month.append(game_times_split_month)
        # 일 자르기
        game_times_split_day = game_times.split('월 ')
        game_times_split_day = game_times_split_day[1].split('일')
        game_times_split_day = game_times_split_day[0]
        day.append(game_times_split_day)


    for i in range(1000):
        myYear = int(year[i])
        myMonth = int(month[i])
        myDay = int(day[i])
        dayOfTheWeek = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        result.append(dayOfTheWeek[date(myYear, myMonth, myDay).weekday()])
        if result[i] == "월요일":
            monday += 1
        elif result[i] == "화요일":
            tuesday += 1
        elif result[i] == "수요일":
            wednesday += 1
        elif result[i] == "목요일":
            thursday += 1
        elif result[i] == "금요일":
            friday += 1
        elif result[i] == "토요일":
            saturday += 1
        else:
            sunday += 1
    print(result)

    # 데이터 프레임
    raw_data = {'monday': monday, 'tuesday': tuesday, 'wednesday': wednesday, 'thursday': thursday, 'friday': friday, 'saturday': saturday, 'sunday': sunday}
    columns = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    row = ['요일별 게임 횟수']

    data = pd.DataFrame([raw_data], index=row, columns=columns)
    
    # 데이터 프레임 출력
    print(data)
    # print(game_times)

    # 데이터 프레임을 JSON으로 저장
    # data.to_json('ThGame.json', orient='table')

    ax = data.plot(kind='bar', title='day of week', figsize=(24, 0), legend=True, fontsize=8)
    ax.set_xlabel('요일', fontsize=8)          # x축 정보 표시
    ax.set_ylabel('count', fontsize=8)     # y축 정보 표시
    ax.legend(['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], fontsize=5)    # 범례 지정
    plt.show()

# 소환사 이름 입력
if __name__ == "__main__":
    set_config()
    parseOPGG("hide on bush")