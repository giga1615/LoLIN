from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

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


    # 소환사 이름 불러오기
    name = soup.select('div.Information > span.Name')[0].get_text()


    # 랭크 유형 불러오기
    rank = soup.select('div.TierRankInfo > div.RankType')[0].get_text()

    # 티어 불러오기
    tier = soup.select('div.TierRankInfo > div.TierRank')[0].get_text()

    # 티어 정보 불러오기
    tierInfo = soup.select('div.TierRankInfo > div.TierInfo > span.LeaguePoints')[0].get_text()

    # 랭크 승 패 승률 불러오기
    winlose = soup.select('div.TierRankInfo > div.TierInfo > span.WinLose')[0].get_text()

    # 최근전적
    recent = soup.select('div.WinRatioTitle')[0].get_text()

    # 최근 KDA
    kdaRatio = soup.select('div.KDARatio')[0].get_text()

    # 최근 모스트 챔피언
    mostChampion = soup.select('td.MostChampion')[0].get_text()

    # 최근 선호 라인
    position = soup.select('td.PositionStats')[0].get_text()

    # 최근 게임
    recentGame = soup.select('div.ItemList')[0].get_text()

    # 데이터 프레임
    raw_data = {'소환사 이름': name, '랭크 종류': rank, '티어': tier, '티어정보': tierInfo, '승패승률': winlose, '최근전적': recent,
                'KDA': kdaRatio, '모스트챔피언': mostChampion, '선호 라인': position, '최근게임': recentGame}

    data = pd.DataFrame(raw_data, index = [0])
    
    # 데이터 프레임 출력
    print(data)

    # 데이터 프레임을 JSON으로 저장
    # data.to_json('recent.json', orient='table')

    # JSON 파일 열기
    # new_data = pd.read_json('recent.json', orient='table')
    # print(new_data)


# 소환사 이름 입력
if __name__ == "__main__":
    
    parseOPGG("hide on bush")
