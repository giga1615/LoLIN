from pandas import DataFrame
from pandas import concat
from selenium import webdriver
from bs4 import BeautifulSoup
from xgboost import XGBRegressor
import pandas as pd
import time
import numpy as np
import numpy
import json


'''
    작성자 : 서울1반 4팀 이도건, 황윤호
    내용 : 유저 추천 알고리즘
    생성일자 : 2021-04-01
    최종수정일자 : 2021-04-02
'''


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
        game_times_split = []
        game_times_split_min = []

        # 오전 오후 나누는 시간 기준
        time_standard = '전'

        result = 0

        # 게임 시간
        all_games_rows = soup.find_all('div', class_='GameItemWrap')

        for all_games_row in all_games_rows:
            game_time_content = all_games_row.find('div', class_='Content')

            game_time_gamestats = game_time_content.find('div', class_='GameStats')

            game_time_timestamp = game_time_gamestats.find('div', class_='TimeStamp')

            game_times = game_time_timestamp.find('span', class_='_timeago _timeCountAssigned tip').get('title')

            # 분
            game_times_split_min = game_times.split('시 ')
            game_times_split_min = game_times_split_min[1].split('분')
            result = int(game_times_split_min[0])


            # 시
            game_times_split = game_times.split('오')
            game_times_split = game_times_split[1].split('시')
            if time_standard in game_times_split[0]:
                game_times_split = game_times_split[0].split('전 ')
                game_times_split = int(game_times_split[1]) * 60
                # 12 * 60
                if game_times_split == 7200:
                    game_times_split = 0
                result += game_times_split
                game_times_list.append(result)
            else:
                game_times_split = game_times_split[0].split('후 ')
                game_times_split = (int(game_times_split[1]) + 12) * 60
                result += game_times_split
                game_times_list.append(result)

            result = 0

        # dataframe 형태

        # 예측 날짜
        days_in = len(game_times_list) // 2
        day_out = 1

        # 게임 시간

        values = numpy.array(game_times_list, dtype=np.float64)

        df = DataFrame(values)

        # 학습을 위한 배열
        raw = []
        
        for i in range(days_in, 0, -1):
            raw.append(df.shift(i))
        
        for i in range(0, day_out):
            raw.append(df.shift(-i))

        # print(raw)
        sum = concat(raw, axis = 1)

        sum.dropna(inplace = True)

        # Supervised Learning 데이터로 변형된 데이터는 train에 저장
        train = sum.values

        # 모델 훈련 및 예측
        trainX, trainy = train[:, :-1], train[:, -1]

        # days_in, n_estimators 값에 따라 예측 값이 달라진다.
        model = XGBRegressor(objective="reg:squarederror", n_estimators=80)
        model.fit(trainX, trainy)

        data_in = values[-(days_in):]

        # 예측 시간
        result = model.predict(np.array([data_in]))

        # json 반환
        data = {
            'TimePredict' : ''
        }

        data['TimePredict'] = result[0]

        data_convert = {k:float(v) for k,v in data.items()}

        json_data = json.dumps(data_convert, ensure_ascii=False)

        print(json_data)

# 소환사 이름 입력
if __name__ == "__main__":
    
    parseOPGG("hide on bush")
    # parseOPGG("렐")