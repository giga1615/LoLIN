import time
import requests
import pandas as pd
import re
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


'''
    작성자 : 서울1반 4팀 황윤호
    내용 : 메인페이지의 미니 프로필
    생성일자 : 2021-04-01
    최종수정일자 : 2021-04-01
'''


def parseOPGG(Name):
    url = 'https://www.op.gg/summoner/userName=' + Name

    driver = webdriver.Chrome('chromedriver.exe')
    
    driver.get(url)

    ## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
    driver.implicitly_wait(3)
    
    resp = driver.page_source
    
    soup = BeautifulSoup(resp, 'html.parser')

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
        wins = '0승'
    else:
        wins = soup.find('span', class_='wins').get_text().strip()

    # 소환사 패 불러오기
    if tier == 'Unranked':
        losses = '0패'
    else:
        losses = soup.find('span', class_='losses').get_text().strip()

    # 소환사 승률 불러오기
    if tier == 'Unranked':
        winRatio = '승률 0%'
    else:
        winRatio = soup.find('span', class_='winratio').get_text().strip()


    # JSON 반환
    data = {
        'nickName' : '',
        'level' : '',
        'tier' : '',
        'tierInfo' : '',
        'wins' : '',
        'losses' : '',
        'winRatio' : '',
    }

    data['nickName'] = nickName
    data['level'] = level
    data['tier'] = tier
    data['tierInfo'] = tierInfo
    data['wins'] = wins
    data['losses'] = losses
    data['winRatio'] = winRatio

    json_data = json.dumps(data, ensure_ascii=False)
    print(json_data)


if __name__ == "__main__":

    # parseOPGG("꼬마자동차 붕봉")
    parseOPGG("렐")
