import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
    작성자 : 서울1반 4팀 황윤호
    내용 : 유저 게임 정보 추출 및 플레이 하지 않은 챔피언 까지 담기
    생성일자 : 2021-03-16
    최종수정일자 : 2021-03-25
'''

# text 형식만 출력하기
def get_data(info):
    if info is None:
        return 'None'
    else:
        return info.get_text().strip()


def parseOPGG(Name):
    url = 'https://www.op.gg/summoner/champions/userName=' + Name

    driver = webdriver.Chrome('chromedriver.exe')
    
    driver.get(url)

    ## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
    driver.implicitly_wait(3)
    
    resp = driver.page_source
    
    soup = BeautifulSoup(resp, 'html.parser')

    # 소환사 이름 불러오기
    name = soup.select('div.Information > span.Name')[0].get_text()

    # 추출한 데이터 저장하기 위한 리스트
    rank_df = []

    # 데이터 프레임 만들기 위한 리스트
    champ_name_list = []
    champ_win_list = []
    champ_lose_list = []
    champ_games_list = []
    champ_win_ratio_list = []
    champ_kda_list = []


    # 솔로/자유 랭크 정보 가져오기
    rank_champ_rows = soup.find_all('tr', role='row')[1:]

    for rank_champ_row in rank_champ_rows:
        # 챔피언 이름
        champ_name = rank_champ_row.find('td', class_='ChampionName Cell').get('data-value')

        # 챔피언 승
        champ_win = get_data(rank_champ_row.find('div', class_='Text Left'))
        # 승이 없다면(None 타입이라면) 0으로 바꾼다.
        if champ_win == 'None':
            champ_win = 0
        # 승 문자열 없애주기
        elif type(champ_win) != 'int':
            champ_win = champ_win.replace('승', '')
        
        # 챔피언 패
        champ_lose = get_data(rank_champ_row.find('div', class_='Text Right'))
        if champ_lose == 'None':
            champ_lose = 0
        elif type(champ_lose) != 'int':
            champ_lose = champ_lose.replace('패', '')

        # 챔피언 판 수
        champ_games = int(champ_win) + int(champ_lose)

        # 챔피언 승률
        # champ_win_ratio = round((int(champ_win) / (int(champ_win) + int(champ_lose))) * 100)
        champ_win_ratio = rank_champ_row.select_one('td:nth-child(4)').get('data-value')

        champ_win_ratio = round(float(champ_win_ratio))

        # 챔피언 평점
        champ_kda = rank_champ_row.select_one('td:nth-child(5)').get('data-value')

        # 데이터 추가
        rank_df.append([champ_name, champ_win, champ_lose, champ_games, champ_win_ratio, champ_kda])
        champ_name_list.append(champ_name)
        champ_win_list.append(champ_win)
        champ_lose_list.append(champ_lose)
        champ_games_list.append(champ_games)
        champ_win_ratio_list.append(champ_win_ratio)
        champ_kda_list.append(champ_kda)

    # 데이터 프레임
    # raw_data = {'챔피언': champ_name, '챔피언 승': champ_win, '챔피언 패': champ_lose, '챔피언 판 수': champ_games, '챔피언 승률(%)': champ_win_ratio, '챔피언 KDA': champ_kda}
    raw_data = {'챔피언 승': champ_win_list, '챔피언 패': champ_lose_list, '챔피언 승률(%)': champ_win_ratio_list, '챔피언 KDA': champ_kda_list}
    columns = ['챔피언 승', '챔피언 패', '챔피언 승률(%)', '챔피언 KDA']

    # 게임을 하지 않았으면 데이터가 없다고 알려준다.
    if len(rank_df) == 0:
        print('데이터가 없습니다.')
    else:
        data = pd.DataFrame(raw_data, index=champ_name_list, columns=columns)
        # data.to_json('UserGameInfo.json', orient='table')
        print(data)

if __name__ == "__main__":

    parseOPGG("hide on bush")
