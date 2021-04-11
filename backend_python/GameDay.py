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

def parseOPGG(Name):

    url = 'https://www.op.gg/summoner/userName=' + Name

    driver = webdriver.Chrome('chromedriver.exe')
    
    
    #헤드리스 시작
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    #options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")

    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    #헤드리스끝
    
    
    driver.get(url)

    ## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
    driver.implicitly_wait(3)
    
    resp = driver.page_source

    # 크롤링 가능 여부 확인
    soup = BeautifulSoup(resp, 'html.parser')

    # 크롤링 가능 여부 확인
    check = ''
    find_string = '기록된 전적이 없습니다.'

    soup_new = soup.prettify()
    result_list = soup_new.split('\n')

    data = {
        'TimePredict' : ''
    }

    for i in result_list:
        if find_string in i:
            i = i.strip()
            check = i 
    
    if find_string == check:
        data['TimePredict'] = check

        json_data = json.dumps(data, ensure_ascii=False)

        print(json_data)

    else:
        xpath = """//*[@id="SummonerRefreshButton"]"""

        try : 
            driver.find_element_by_xpath(xpath).click() # 최근전적으로 갱신하기
        except :#검색안된경우 fail보내줘서 interceptor가 알아들을 수 있게함
            data['TimePredict'] = 'Fail'

            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)

        time.sleep(10)
        
        #아래처럼 하는게 안정성이 더높음, 적을때, 무한루프 걸리지않고,
        #오버해서 검색하지도 않음 딱적정하게 됨, 더 빨리 할 수 있으나 안전성 문제가 있음, 예외처리가 나거나
        #안불러와지는경우가있음

        try :
            while True :
                try:
                    driver.find_element_by_css_selector('.GameMoreButton').click()
                    message1=driver.find_element_by_css_selector('.ErrorMessage > div').text
                    
                    if message1 == "기록된 전적이 없습니다." :
                        print("빠르게 제대로 찾았는지확인")
                        break
                except:
                    continue
        except:
            return HttpResponse("Fail")
    
   
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


    for i in range(len(all_games_rows)):
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

    # ax = data.plot(kind='bar', title='day of week', figsize=(24, 0), legend=True, fontsize=8)
    # ax.set_xlabel('요일', fontsize=8)          # x축 정보 표시
    # ax.set_ylabel('count', fontsize=8)     # y축 정보 표시
    # ax.legend(['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], fontsize=5)    # 범례 지정
    # plt.show()
    x = np.arange(7)
    dayOfWeek = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    values = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

    plt.bar(x, values, width=0.6, align='edge', color="blue",
        edgecolor="black", linewidth=3, tick_label=dayOfWeek)

    fig = plt.gcf() #변경한 곳
    plt.show()
    # fig.savefig('DayOfWeek.png')

# 소환사 이름 입력
if __name__ == "__main__":
    parseOPGG("hide on bush")