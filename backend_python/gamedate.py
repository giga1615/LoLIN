from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
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
    game_times_split = []
    # 오전 오후 나누는 시간 기준
    time_standard = '전'

    # 게임 시간
    all_games_rows = soup.find_all('div', class_='GameItemWrap')

    for all_games_row in all_games_rows:
        game_time_content = all_games_row.find('div', class_='Content')

        game_time_gamestats = game_time_content.find('div', class_='GameStats')

        game_time_timestamp = game_time_gamestats.find('div', class_='TimeStamp')

        game_times = game_time_timestamp.find('span', class_='_timeago _timeCountAssigned tip').get('title')

        game_times_split = game_times.split('오')
        game_times_split = game_times_split[1].split('시')
        if time_standard in game_times_split[0]:
            game_times_split = game_times_split[0].split('전 ')
            game_times_split = int(game_times_split[1])
            if game_times_split == 12:
                game_times_split = 0
            game_times_list.append(game_times_split)
        else:
            game_times_split = game_times_split[0].split('후 ')
            game_times_split = int(game_times_split[1]) + 12
            game_times_list.append(game_times_split)

        # game_time.append(game_time)
    # print(len(all_games_rows))
    # 0
    zero = []
    zero_cnt = 0
    # 1
    one = []
    one_cnt = 0
    # 2
    two = []
    two_cnt = 0
    # 3
    three = []
    three_cnt = 0
    # 4
    four = []
    four_cnt = 0
    # 5
    five = []
    five_cnt = 0
    # 6
    six = []
    six_cnt = 0
    # 7
    seven = []
    seven_cnt = 0
    # 8
    eight = []
    eight_cnt = 0
    # 9
    nine = []
    nine_cnt = 0
    # 10
    ten = []
    ten_cnt = 0
    # 11
    eleven = []
    eleven_cnt = 0
    # 12
    twelve = []
    twelve_cnt = 0
    # 13
    thirteen = []
    thirteen_cnt = 0
    # 14
    fourteen = []
    fourteen_cnt = 0
    # 15
    fifteen = []
    fifteen_cnt = 0
    # 16
    sixteen = []
    sixteen_cnt = 0
    # 17
    seventeen = []
    seventeen_cnt = 0
    # 18
    eighteen = []
    eighteen_cnt = 0
    # 19
    nineteen = []
    nineteen_cnt = 0
    # 20
    twenty = []
    twenty_cnt = 0
    # 21
    twentyone = []
    twentyone_cnt = 0
    # 22
    twentytwo = []
    twentytwo_cnt = 0
    # 23
    twentythree = []
    twentythree_cnt = 0


    # 데이터 분류
    for i in range(len(game_times_list)):
        if game_times_list[i] == 0:
            zero_cnt += 1
        elif game_times_list[i] == 1:
            one_cnt += 1
        elif game_times_list[i] == 2:
            two_cnt += 1
        elif game_times_list[i] == 3:
            three_cnt += 1
        elif game_times_list[i] == 4:
            four_cnt += 1
        elif game_times_list[i] == 5:
            five_cnt += 1
        elif game_times_list[i] == 6:
            six_cnt += 1
        elif game_times_list[i] == 7:
            seven_cnt += 1
        elif game_times_list[i] == 8:
            eight_cnt += 1
        elif game_times_list[i] == 9:
            nine_cnt += 1
        elif game_times_list[i] == 10:
            ten_cnt += 1
        elif game_times_list[i] == 11:
            eleven_cnt += 1
        elif game_times_list[i] == 12:
            twelve_cnt += 1
        elif game_times_list[i] == 13:
            thirteen_cnt += 1
        elif game_times_list[i] == 14:
            fourteen_cnt += 1
        elif game_times_list[i] == 15:
            fifteen_cnt += 1
        elif game_times_list[i] == 16:
            sixteen_cnt += 1
        elif game_times_list[i] == 17:
            seventeen_cnt += 1
        elif game_times_list[i] == 18:
            eighteen_cnt += 1
        elif game_times_list[i] == 19:
            nineteen_cnt += 1
        elif game_times_list[i] == 20:
            twenty_cnt += 1
        elif game_times_list[i] == 21:
            twentyone_cnt += 1
        elif game_times_list[i] == 22:
            twentytwo_cnt += 1
        else:
            twentythree_cnt += 1

    # 데이터 프레임
    raw_data = {'zero': zero_cnt, 'one': one_cnt, 'two': two_cnt, 'three': three_cnt, 'four': four_cnt, 'five': five_cnt, 'six': six_cnt,'seven': seven_cnt, 'eight':eight_cnt, 'nine': nine_cnt, 'ten': ten_cnt, 'eleven': eleven_cnt, 'twelve': twelve_cnt, 'thirteen': thirteen_cnt, 'fourteen': fourteen_cnt, 'fifteen': fifteen_cnt, 'sixteen':sixteen_cnt, 'seventeen':seventeen_cnt, 'eighteen': eighteen_cnt, 'nineteen': nineteen_cnt, 'twenty': twenty_cnt, 'twentyone': twentyone_cnt, 'twentytwo': twentytwo_cnt, 'twentythree': twentythree_cnt}
    columns = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twentyone','twentytwo','twentythree']
    row = ['해당 시간 게임 이용 횟수']

    data = pd.DataFrame(raw_data, index=row, columns=columns)
    
    # 데이터 프레임 출력
    print(data)
    # print(game_times_list)

    # 데이터 프레임을 JSON으로 저장
    # data.to_json('GameDate.json', orient='table')
    # ax = data.plot(kind='bar', title='GameDate', figsize=(24, 0), legend=True, fontsize=8)
    # ax.set_xlabel('0 ~ 23', fontsize=8)          # x축 정보 표시
    # ax.set_ylabel('count', fontsize=8)     # y축 정보 표시
    # ax.legend(['zero','one', 'two', 'three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twentyone','twentytwo','twentythree'], fontsize=5)    # 범례 지정
    # plt.show()

    x = np.arange(24)
    dayOfTime = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twentyone','twentytwo','twentythree']
    values = [zero_cnt, one_cnt, two_cnt, three_cnt, four_cnt, five_cnt, six_cnt, seven_cnt, eight_cnt, nine_cnt, ten_cnt, eleven_cnt, twelve_cnt, thirteen_cnt, fourteen_cnt, fifteen_cnt, sixteen_cnt, seventeen_cnt, eighteen_cnt, nineteen_cnt, twenty_cnt, twentyone_cnt, twentytwo_cnt, twentythree_cnt]

    plt.bar(x, values, width=0.6, align='edge', color="red",
        edgecolor="black", linewidth=3, tick_label=dayOfTime)

    fig = plt.gcf() #변경한 곳
    plt.show()
    fig.savefig('DayOfTime.png')

# 소환사 이름 입력
if __name__ == "__main__":
    parseOPGG("꼬마자동차 붕봉")