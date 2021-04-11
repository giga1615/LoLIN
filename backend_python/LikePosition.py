from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import json

'''
    작성자 : 서울1반 4팀 황윤호
    내용 : 선호하는 포지션 추출 및 json반환
    생성일자 : 2021-03-15
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
    
    soup = BeautifulSoup(resp, 'html.parser')

    # 크롤링 가능 여부 확인
    result = ''
    find_string = '기록된 전적이 없습니다.'

    soup_new = soup.prettify()
    result_list = soup_new.split('\n')

    for i in result_list:
        if find_string in i:
            i = i.strip()
            result = i
        
    # 소환사 이름 불러오기
    nickName = soup.select('div.Information > span.Name')[0].get_text().strip()

    # 선호 포지션 불러오기
    if find_string != result:
        position = soup.select('div.PositionStatContent > div.Name')[0].get_text().strip()
    else:
        position = '경기 기록이 없습니다.'
    # json 반환
    data = {
        'nickName' : '',
        'LikePosition' : ''
    }

    data['nickName'] = nickName
    data['LikePosition'] = position

    json_data = json.dumps(data, ensure_ascii=False)

    print(json_data)


# 소환사 이름 입력
if __name__ == "__main__":
    
    parseOPGG("hide on bush")
