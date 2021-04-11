from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
import requests
import json


'''
    작성자 : 서울1반 4팀 황윤호
    내용 : 인게임 정보 분석 후 승률 예측(함수 통합)
    생성일자 : 2021-03-15
    최종수정일자 : 2021-04-03
'''


def ingameOPGG(Name):

    # 갱신하기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(options=options)
    url = 'https://www.op.gg/summoner/userName=' + Name
    action = ActionChains(driver)
    driver.get(url)

    try:
        driver.find_element_by_css_selector('.Button.SemiRound.Blue').click()
        action.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as ex:
        print("exception: ", ex)
        driver.quit()
    driver.quit()

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

    # 레드팀 포인트
    Rt_point = 0


    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(options=options)
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

    if len(names) == 0:
        return Container

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
        })
        data['레드팀'].append({
            "nickName" : Rt_nickName[i],
            "tier" : Rt_tier[i],
            "tierImg" : Rt_tier_img[i],
            "rankWinRate" : Rt_rank_ori[i],
            "champWinRate" : Rt_champ_ori[i],
            "kda" : Rt_kda_ori[i],
        })

    data['블루팀'].append({
        "Bt_point" : Bt_point
    })
    data['레드팀'].append({
        "Rt_point" : Rt_point
    })

    json_data = json.dumps(data, ensure_ascii=False)

    print(json_data)


if __name__ == "__main__":
    ingameOPGG("2000 02 09")