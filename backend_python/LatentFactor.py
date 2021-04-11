import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
    작성자 : 서울1반 4팀 황윤호
    내용 : 게임 데이터 LatentFactorModel 적용
    생성일자 : 2021-03-23
    최종수정일자 : 2021-03-23
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
    
    # 모든 챔피언
    champ_all_list = ['누누와 윌럼프', '라이즈', '마스터 이', '모르가나', '사이온', '소라카', '시비르', '알리스타', '애니', '애쉬', '워윅', '잭스', '케일', '트리스타나', 
    '트위스티드 페이트', '티모', '피들스틱', '신지드', '질리언', '이블린', '트린다미어', '트위치', '카서스', '아무무', '초가스', '람머스', '애니비아', '베이가', '카사딘', '갱플랭크', '타릭',
    '말파이트', '문도 박사', '블리츠크랭크', '잔나', '카타리나', '코르키', '나서스', '샤코', '하이머딩거', '우디르', '니달리', '뽀삐', '그라가스', '판테온', '모데카이저', '이즈리얼', 
    '쉔', '케넨', '가렌', '아칼리', '말자하', '올라프', '코그모', '신 짜오', '블라디미르', '갈리오', '우르곳', '미스 포츈', '소나', '스웨인', '럭스', '르블랑', '이렐리아', '트런들', 
    '카시오페아', '케이틀린', '레넥톤', '카르마', '마오카이', '자르반 4세', '녹턴', '리 신', '브랜드', '럼블', '베인', '오리아나', '요릭',  '레오나', '오공', '스카너', '탈론', '리븐', 
    '제라스', '그레이브즈', '쉬바나', '피즈', '볼리베어', '아리', '빅토르', '세주아니', '직스', '노틸러스', '피오라', '룰루', '헤카림', '바루스', '다리우스', '드레이븐', '제이스', '자이라', 
    '다이애나', '렝가', '신드라', '카직스', '엘리스', '제드', '나미', '바이', '쓰레쉬', '퀸', '자크', '리산드라', '아트록스', '루시안', '징크스', '야스오', '벨코즈', '브라움', '나르', 
    '아지르', '칼리스타', '렉사이', '바드', '에코', '탐 켄치', '킨드레드', '일라오이', '진', '아우렐리온 솔', '탈리야', '클레드', '아이번', '카밀', '자야', '라칸', '케인', '오른', '조이', 
    '카이사', '파이크', '니코', '사일러스', '유미', '키아나', '세나', '아펠리오스', '세트', '릴리아', '요네', '사미라', '세라핀', '렐', '비에고', 
    ]

    # 플레이하지 않은 챔피언 추가하기
    for i in range(len(champ_all_list)):
        if champ_all_list[i] not in champ_name_list:
            champ_name_list.append(champ_all_list[i])

    # 서로 다른 길이의 리스트를 데이터 프레임으로 만드는 과정
    dic = {
        '챔피언 이름' : champ_name_list,
        '챔피언 승' : champ_win_list,
        '챔피언 패' : champ_lose_list,
        '챔피언 승률(%)' : champ_win_ratio_list,
        '챔피언 KDA' : champ_kda_list
    }

    # 게임을 하지 않았으면 데이터가 없다고 알려준다.
    if len(rank_df) == 0:
        print('데이터가 없습니다.')
    else:
        # 딕셔너리를 데이터프레임 형식으로
        data = pd.DataFrame.from_dict(dic, orient='index')
        # 행과 열 바꾸기
        data = data.transpose()

        # data_i 잠재 인수 모델을 적용하기 위한 데이터프레임 (챔피언 승률 예측)
        data_i = data.set_index('챔피언 이름')
        print(data_i)

        # 챔피언 별 역할군을 토대로 승률을 예측한다.


if __name__ == "__main__":

    parseOPGG("hide on bush")
