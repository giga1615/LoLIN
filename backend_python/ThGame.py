from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

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

        # 분 시 합치기

        

        # game_time.append(game_time)
    # print(game_times_list)
    # print(len(all_games_rows))
    # # 06~14
    # morning = []
    # morning_cnt = 0
    # # 14~22
    # lunch = []
    # lunch_cnt = 0
    # # 22~06
    # evening = []
    # evening_cnt = 0

    # 데이터 분류
    # for i in range(len(game_times_list)):
    #     if game_times_list[i] > 6 and game_times_list[i] <= 14:
    #         morning_cnt += 1
    #     elif game_times_list[i] > 14 and game_times_list[i] <= 22:
    #         lunch_cnt += 1
    #     else:
    #         evening_cnt += 1

    # 1000
    # columns = []
    # raw_data = []
    # for i in range(1, 1001):
    #     columns.append(i)


    # 데이터 프레임
    # raw_data = {'columns': game_times_list}
    # columns = ['cnt']
    # row = ['N번째 경기 시작한 시간']

    # data = pd.DataFrame([raw_data], index=row, columns=columns)
    data = pd.DataFrame(result)
    
    # 데이터 프레임 출력
    print(data)
    # print(game_times)

    # 데이터 프레임을 JSON으로 저장
    # data.to_json('ThGame.json', orient='table')



# 소환사 이름 입력
if __name__ == "__main__":
    
    parseOPGG("hide on bush")