import json
import math
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from django.http import HttpResponse

import time
import requests
import pandas as pd
import re
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pandas import DataFrame
from pandas import concat
from xgboost import XGBRegressor
import numpy as np
import numpy

from .models import MemberForRecommend
from selenium.webdriver.common.action_chains import ActionChains





# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    return HttpResponse("my_to_do_app first page")


@api_view(['GET', 'POST'])
def memberInfo(request):

    # JSON 반환
    data = {
        'nickName' : '',
        'level' : '',
        'tier' : '',
        'tierInfo' : '',
        'wins' : '',
        'losses' : '',
        'winRatio' : '',
        'LikePosition' : '',
         
    }

    searchName=request.GET["BangJang"]
    Name=searchName
    searchName=searchName.replace(" ", "")

    print(Name)
    url = 'https://www.op.gg/summoner/userName=' + searchName

    
    
       #헤드리스 시작
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    

    driver = webdriver.Chrome('/home/ubuntu/django/mysite/chromedriver', options=options)
    #헤드리스끝
    

 
    
    driver.get(url)

    ## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
    driver.implicitly_wait(3)
    
    resp = driver.page_source
    
    soup = BeautifulSoup(resp, 'html.parser')
    
    
    
    #
    
    result = ''
    find_string = '기록된 전적이 없습니다.'

    try :
        position=driver.find_element_by_css_selector('.PositionStatContent > .Name').text
    except :
        position="선호하는 포지션이 없습니다."
    
    #except랑 다르게 아예정보없는 사람말고 정보는 있는데 몇판안해서 이럴수 있음
    if position == "" :
        data['LikePosition'] = "선호하는 포지션이 없습니다."    
    else :
        data['LikePosition'] = position

    

    

    # 소환사 이름 불러오기
    nickName = soup.select('div.Information > span.Name')[0].get_text().strip()

    # 소환사 레벨 불러오기
    level = soup.find('span', class_='Level tip').get_text().strip()

    '''
    아래는 모두 솔로랭크 데이터
    '''
    # 소환사 티어 불러오기
    tier = soup.find('div', class_='TierRank').get_text().strip()

    # 소환사 상세 티어 정보 불러오기
    # 만약 언랭이라면 언랭으로 표시
    if tier == 'Unranked':
        tierInfo = '0 LP'
    # 랭크가 있으면 랭크 표시
    else:
        tierInfo = soup.find('span', class_='LeaguePoints').get_text().strip()

    # 소환사 승 불러오기
    if tier == 'Unranked':
        wins = '0'
    else:
        wins = soup.find('span', class_='wins').get_text().strip()

    # 소환사 패 불러오기
    if tier == 'Unranked':
        losses = '0'
    else:
        losses = soup.find('span', class_='losses').get_text().strip()

    # 소환사 승률 불러오기
    if tier == 'Unranked':
        winRatio = '승률 0%'
    else:
        winRatio = soup.find('span', class_='winratio').get_text().strip()


    

    data['nickName'] = Name
    data['level'] = level
    data['tier'] = tier.split(' ')[0]
    data['tierInfo'] = tierInfo
    data['wins'] = wins.replace("W","")
    data['losses'] = losses.replace("L","")
    data['winRatio'] = winRatio
    

    json_data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(json_data)

@api_view(['GET', 'POST'])
def predictTime(request):



    searchName=request.GET["BangJang"]
    Name=searchName
    searchName=Name.replace(" ", "")

    print("실행이잘되고 있는건지1")
    hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}


    url = 'https://www.op.gg/summoner/userName=' + searchName

    
    print("실행이잘되고 있는건지2")
    #헤드리스 시작
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    # 속도 향상을 위한 옵션 해제
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome('/home/ubuntu/django/mysite/chromedriver', options=options)
    #헤드리스끝
    print("실행이잘되고 있는건지3")
    
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
    print("실행이잘되고 있는건지4")
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
        
        
        #아래처럼 하는게 안정성이 더높음, 적을때, 무한루프 걸리지않고,
        #오버해서 검색하지도 않음 딱적정하게 됨, 더 빨리 할 수 있으나 안전성 문제가 있음, 예외처리가 나거나
        #안불러와지는경우가있음

        try :
            while True :
                try:
                    print("실행이잘되고 있는건지5클릭 클릭")
                    try:
                        driver.find_element_by_css_selector('.GameMoreButton').click()
                    except:
                        print("이 예외는 클릭을 못하는겁니다.")
                        break;
                    try:
                        message1=driver.find_element_by_css_selector('.ErrorMessage > div').text
                    except:
                        print("이예외는 끝이나야 끝납니다.")
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
        game_times_split_a=[]
        game_times_split_b=[]
        game_times_split_min = []

        # 오전 오후 나누는 시간 기준
        time_standard = 'A'

        result = 0

        # 게임 시간
        all_games_rows = soup.find_all('div', class_='GameItemWrap')

    
        if len(all_games_rows) > 1000 :
            all_games_rows = all_games_rows[:1000]

        print(len(all_games_rows))

        for all_games_row in all_games_rows:
            
            game_time_content = all_games_row.find('div', class_='Content')

            game_time_gamestats = game_time_content.find('div', class_='GameStats')

            game_time_timestamp = game_time_gamestats.find('div', class_='TimeStamp')

            game_times = game_time_timestamp.find('span', class_='_timeago _timeCountAssigned tip').get('title')

           # print(game_times)
        
            # 분
            game_times_split_min = game_times.split(':')
            game_times_split_min = game_times_split_min[1].split(' ')
            result = int(game_times_split_min[0])
        


            # 시
            game_times_split = game_times.split(' ')
            game_times_split_a = game_times_split[3]
            game_times_split_a = game_times_split_a.split(':')
            game_times_split_a = game_times_split_a[0]

            game_times_split_b = game_times_split[4]

            #오전
            if time_standard in game_times_split_b:
                game_times_split = int(game_times_split_a) * 60
                # 12 * 60
                if game_times_split == 7200:
                    game_times_split = 0
                result += game_times_split
                game_times_list.append(result)
            else:#오후  
                game_times_split = (int(game_times_split_a) + 12) * 60
                result += game_times_split
                game_times_list.append(result)
            print(result)
            result = 0

        # dataframe 형태

        print("실행이잘되고 있는건지5")
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
        print("실행이잘되고 있는건지6")

        data['TimePredict'] = math.floor(result[0]/60)
    
        temp_123=0;
        if math.floor(result[0]/60) == 24 :
            temp_123=0
        else :
            temp_123=math.floor(result[0]/60)

        member = MemberForRecommend.objects.filter(nickname=Name)
        member.update(time_predict=math.floor(temp_123))
        

        data_convert = {k:float(v) for k,v in data.items()}

        json_data = json.dumps(data_convert, ensure_ascii=False)
        
        driver.close()
        print("실행이잘되고 있는건지7")

    print(json_data)
    print("계산끝_db저장되었을거임")



    return HttpResponse(json_data)





@api_view(['GET', 'POST'])
def Ingame(request):

    Name=request.GET["nickName"]
    
    searchName=Name.replace(" ", "")

    Name=searchName

        # 갱신하기
       #헤드리스 시작
 #   options = webdriver.ChromeOptions()
 #   options.add_argument('headless')
 #   options.add_argument('--no-sandbox')
 #   options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    
  
# 속도 향상을 위한 옵션 해제
    #prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
 #   options.add_experimental_option('prefs', prefs)
 #   driver = webdriver.Chrome('/home/ubuntu/django/mysite/chromedriver', options=options)
    #헤드리스끝
    

    
    #url = 'https://www.op.gg/summoner/userName=' + Name
    #action = ActionChains(driver)
    #driver.get(url)

    
    #try:
    #    driver.find_element_by_css_selector('.Button.SemiRound.Blue').click()
    #    action.send_keys(Keys.ENTER)
    #    time.sleep(1)
    #except Exception as ex:
    #    print("exception: ", ex)
    #    driver.quit()
   # #driver.quit()

    # 블루팀 닉네임
    Bt_nickName = []
    # 블루팀 티어
    Bt_tier = []
    # 블루팀 티어 이미지
    Bt_tier_img = []
    # 블루팀 랭크 승률
    Bt_rank = []
    # 블루팀 챔피언 승률
    Bt_champ = []
    # 블루팀 kda
    Bt_kda = []
    # 블루팀 챔프
    Bt_champName = []

    # 블루팀 포인트
    Bt_point = 0

    # 레드팀 닉네임
    Rt_nickName = []
    # 레드팀 티어
    Rt_tier  = []
    # 레드팀 티어 이미지
    Rt_tier_img = []
    # 레드팀 랭크 승률
    Rt_rank = []
    # 레드팀 챔피언 승률
    Rt_champ = []
    # 레드팀 kda
    Rt_kda = []

    # 레드팀 챔프
    Rt_champName = []

    # 레드팀 포인트
    Rt_point = 0


       #헤드리스 시작
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
    options.add_experimental_option('prefs', prefs)


    driver = webdriver.Chrome('/home/ubuntu/django/mysite/chromedriver', options=options)
    #헤드리스끝
    

    

    # driver = webdriver.Chrome()
    url = 'https://www.op.gg/summoner/userName=' + Name
   

    driver.get(url)
  
    
    
    Container = {}

 
    
    driver.find_element_by_css_selector('.SpectateTabButton').click()
 
    time.sleep(5)
    

   
    html = driver.page_source
  

    soup = BeautifulSoup(html, 'html.parser')
 
  
    link = soup.find("link").attrs['href']

    Container['Link'] = link
   
    
    ingameInfo = soup.find("div", {"class" : "tabItem Content SummonerLayoutContent summonerLayout-spectator"})
  
    names = ingameInfo.find_all("td", {"class" : "SummonerName Cell"})

    Container['Names'] = []
 
 
    #return containor는 에러 발생시킴
    if len(names) == 0:
        abc="fail"
        json_data = json.dumps(abc, ensure_ascii=False)
        return HttpResponse(json_data)


    for name in names:
        Container['Names'].append(name.text.strip())
    Bt_nickName = Container['Names'][0:5]
    Rt_nickName = Container['Names'][5:]
 
    # 플레이 하는 챔피언
    champions = ingameInfo.find_all("td", {"class" : "ChampionImage Cell"})
    Container['Champions'] = []
    for champion in champions:
        champ = str(champion.find("a").attrs['href'])
        champ = champ.replace("/champion/", '').replace("/statistics", '').capitalize()
        Container['Champions'].append(champ)
    Bt_champName = Container['Champions'][0:5]
    Rt_champName = Container['Champions'][5:]
    # 티어
    tiers = ingameInfo.find_all("td", {"class" : "CurrentSeasonTierRank Cell"})
    Container['Tiers'] = []
    for tier in tiers:
        Container['Tiers'].append(tier.text.strip())
    Bt_tier = Container['Tiers'][0:5]
    Rt_tier = Container['Tiers'][5:]

    # 티어 이미지
    tiers_imgs = ingameInfo.find_all("td", {"class" : "CurrentSeasonTier Cell"})
    Container['Tiers_imgs'] = []
    #     Container['Tiers_imgs'].append()
    for tiers_img in tiers_imgs:
        if tiers_img.find("img", class_='Image tip') == None:
            Container['Tiers_imgs'].append(tiers_img.find("img", class_='Image tip'))
        else:
            Container['Tiers_imgs'].append(tiers_img.find("img", class_='Image tip').get('src'))
    Bt_tier_img = Container['Tiers_imgs'][0:5]
    Rt_tier_img = Container['Tiers_imgs'][5:]
    


    # 랭크 승률
    ratios = ingameInfo.find_all("td", {"class" : "RankedWinRatio Cell"})
    Container['Ratios'] = []
    for ratio in ratios:
        Container['Ratios'].append(ratio.text.replace('\n', '').replace('\t', '').strip().split('%')[0])
    Bt_rank = Container['Ratios'][0:5]
    Rt_rank = Container['Ratios'][5:]

    Bt_rank_ori = Bt_rank
    Rt_rank_ori = Rt_rank

    # 챔피언 승률 및 KDA
    champRatios = ingameInfo.find_all("td", {"class" : "ChampionInfo Cell"})
    Container['Champion Ratios'] = []
    for champRatio in champRatios:
        Container['Champion Ratios'].append(champRatio.text.replace(' ', '').replace('\n', '').replace('\t', '').strip())
    Bt_champ = Container['Champion Ratios'][0:9:2]
    Bt_kda = Container['Champion Ratios'][1:10:2]
    Rt_champ = Container['Champion Ratios'][10:19:2]
    Rt_kda = Container['Champion Ratios'][11:20:2]

    Bt_champ_ori = Bt_champ
    Bt_kda_ori = Bt_kda
    Rt_champ_ori = Rt_champ
    Rt_kda_ori = Rt_kda

    driver.quit()

    # 블루팀 티어 별 점수
    for tier in Bt_tier:
        if 'Challenger' in tier:
            Bt_point += 10
        elif 'Grandmaster' in tier:
            Bt_point += 9
        elif 'Master' in tier:
            Bt_point += 8
        elif 'Diamond 1' or 'Diamond 2' in tier:
            Bt_point += 7
        elif 'Diamond 3' or 'Diamond 4' in tier:
            Bt_point += 6
        elif 'Platinum' in tier:
            Bt_point += 5
        elif 'Gold' in tier:
            Bt_point += 4
        elif 'Silver' in tier:
            Bt_point += 3
        elif 'Bronze' in tier:
            Bt_point += 2
        else:
            Bt_point += 0
    
    #레드팀 티어 별 점수
    for tier in Rt_tier:
        if 'Challenger' in tier:
            Rt_point += 10
        elif 'Grandmaster' in tier:
            Rt_point += 9
        elif 'Master' in tier:
            Rt_point += 8
        elif 'Diamond 1' or 'Diamond 2' in tier:
            Rt_point += 7
        elif 'Diamond 3' or 'Diamond 4' in tier:
            Rt_point += 6
        elif 'Platinum' in tier:
            Rt_point += 5
        elif 'Gold' in tier:
            Rt_point += 4
        elif 'Silver' in tier:
            Rt_point += 3
        elif 'Bronze' in tier:
            Rt_point += 2
        else:
            Rt_point += 0

    # 블루팀 랭크 승률 없는 기록 제거
    Bt_rank_count = Bt_rank.count('-')

    Bt_rank = list(filter(('-').__ne__, Bt_rank))

    Bt_point += (Bt_rank_count * 5)
    
    # 블루팀 랭크 승률 별 점수
    for rank in Bt_rank:
        if 60 <= int(rank) <= 100:
            Bt_point += 10
        elif 55 <= int(rank) < 60:
            Bt_point += 8
        elif 50 <= int(rank) < 55:
            Bt_point += 6
        elif 45 <= int(rank) < 50:
            Bt_point += 4
        elif 40 <= int(rank) < 45:
            Bt_point += 2
        elif 0 <= int(rank) < 40:
            Bt_point += 0

    # 레드팀 랭크 승률 없는 기록 제거
    Rt_rank_count = Rt_rank.count('-')

    Rt_rank = list(filter(('-').__ne__, Rt_rank))

    Rt_point += (Rt_rank_count * 5)


    # 레드팀 랭크 승률 별 점수
    for rank in Rt_rank:
        if 60 <= int(rank) <= 100:
            Rt_point += 10
        elif 55 <= int(rank) < 60:
            Rt_point += 8
        elif 50 <= int(rank) < 55:
            Rt_point += 6
        elif 45 <= int(rank) < 50:
            Rt_point += 4
        elif 40 <= int(rank) < 45:
            Rt_point += 2
        elif 0 <= int(rank) < 40:
            Rt_point += 0

    # 블루팀 챔피언 승률
    Bt_champ_rate = []
    for champ in Bt_champ:
        Bt_champ_rate.append(champ.split('%')[0])

    # 블루팀 챔피언 승률 없는 데이터 제거
    Bt_champ_count = Bt_champ_rate.count('-')

    Bt_champ_rate = list(filter(('-').__ne__, Bt_champ_rate))

    Bt_point += Bt_champ_count * 5


    # 레드팀 챔피언 승률
    Rt_champ_rate = []
    for champ in Rt_champ:
        Rt_champ_rate.append(champ.split('%')[0])

    # 레드팀 챔피언 승률 없는 데이터 제거
    Rt_champ_count = Rt_champ_rate.count('-')

    Rt_champ_rate = list(filter(('-').__ne__, Rt_champ_rate))

    Rt_point += Rt_champ_count * 5

    # 블루팀 챔피언 승률 별 점수
    for rank in Bt_champ_rate:
        if 60 <= int(rank) <= 100:
            Bt_point += 10
        elif 55 <= int(rank) < 60:
            Bt_point += 8
        elif 50 <= int(rank) < 55:
            Bt_point += 6
        elif 45 <= int(rank) < 50:
            Bt_point += 4
        elif 40 <= int(rank) < 45:
            Bt_point += 2
        elif 0 <= int(rank) < 40:
            Bt_point += 0

    # 레드팀 챔피언 승률 별 점수
    for rank in Rt_champ_rate:
        if 60 <= int(rank) <= 100:
            Rt_point += 10
        elif 55 <= int(rank) < 60:
            Rt_point += 8
        elif 50 <= int(rank) < 55:
            Rt_point += 6
        elif 45 <= int(rank) < 50:
            Rt_point += 4
        elif 40 <= int(rank) < 45:
            Rt_point += 2
        elif 0 <= int(rank) < 40:
            Rt_point += 0

    # 없는 값 점수화 후 블루팀 KDA 없는 값 제거
    Bt_kda_count = Bt_kda.count('-')

    Bt_kda = list(filter(('-').__ne__, Bt_kda))
    
    Bt_point += Bt_kda_count * 2


    # 레드팀 KDA 없는 값 제거
    Rt_kda_count = Rt_kda.count('-')
    
    Rt_kda = list(filter(('-').__ne__, Rt_kda))

    Rt_point += Rt_kda_count * 2

    # 블루팀 KDA 별 점수
    for kda in Bt_kda:
        if kda.split('KDA')[0] == "Perfect" or float(kda.split('KDA')[0]) >= 6:
            Bt_point += 3
        if kda.split('KDA')[0] != "Perfect" and 3 <= float(kda.split('KDA')[0]) < 6:
            Bt_point += 2
        elif kda.split('KDA')[0] != "Perfect" and 1 <= float(kda.split('KDA')[0]) < 3:
            Bt_point += 1
        elif kda.split('KDA')[0] != "Perfect" and 0 <= float(kda.split('KDA')[0]) < 1:
            Bt_point += 0

    # 레드팀 KDA 별 점수
    for kda in Rt_kda:
        if kda.split('KDA')[0] == "Perfect" or float(kda.split('KDA')[0]) >= 6:
            Rt_point += 3
        if kda.split('KDA')[0] != "Perfect" and 3 <= float(kda.split('KDA')[0]) < 6:
            Rt_point += 2
        elif kda.split('KDA')[0] != "Perfect" and 1 <= float(kda.split('KDA')[0]) < 3:
            Rt_point += 1
        elif kda.split('KDA')[0] != "Perfect" and 0 <= float(kda.split('KDA')[0]) < 1:
            Rt_point += 0


    # JSON 반환
    data = {}

    data['블루팀'] = []
    data['레드팀'] = []

    for i in range(5):
        data['블루팀'].append({
            "nickName" : Bt_nickName[i],
            "tier" : Bt_tier[i],
            "tierImg" : Bt_tier_img[i],
            "rankWinRate" : Bt_rank_ori[i],
            "champWinRate" : Bt_champ_ori[i],
            "kda" : Bt_kda_ori[i],
            "champName" : Bt_champName[i],
        })
        data['레드팀'].append({
            "nickName" : Rt_nickName[i],
            "tier" : Rt_tier[i],
            "tierImg" : Rt_tier_img[i],
            "rankWinRate" : Rt_rank_ori[i],
            "champWinRate" : Rt_champ_ori[i],
            "kda" : Rt_kda_ori[i],
            "champName" : Rt_champName[i],
        })

    data['블루팀'].append({
        "Bt_point" : Bt_point
    })
    data['레드팀'].append({
        "Rt_point" : Rt_point
    })

    json_data = json.dumps(data, ensure_ascii=False)

  
    return HttpResponse(json_data)

