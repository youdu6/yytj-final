import requests
from bs4 import BeautifulSoup
import bs4

from util.database import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}

base_country_url = "https://www.dongqiudi.com/team/"
base_play_url = "https://www.dongqiudi.com/player/"
html = ".html"


def getPlayers(country_num, country_name):
    url = base_country_url + country_num + html
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")
    flag = False
    player_id = {}
    soup2 = BeautifulSoup(r.text, "html.parser")
    script = str(soup2.select("body script")[1].contents[0])

    for players in soup.find_all(class_="analysis-list-item"):
        if not flag:
            flag = True
        else:
            role = players.contents[0].contents[0].contents[0]
            name = players.contents[0].contents[2].contents[1]
            n_index = script.find(str(name))
            id_index = script[n_index - 220:].find("person_id")
            person_id = script[n_index - 220 + id_index + 11:n_index - 220 + id_index + 11 + 8]
            # print(person_id)

            player_id[str(name)] = str(person_id)
            print(country_name + " " + str(name) + " " + str(role))
    return player_id


def getCap(play_number, name, country):
    url = base_play_url + play_number + html

    role = ''
    capability = {}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    flag = False

    if soup.find(class_="china-name") is None:
        print(name + " " + country)
        print("无数据")
        print()
        return None
    name = soup.find(class_="china-name").contents[0]
    # print(name)
    if len(soup.find(class_="second-ul").contents[0].contents) == 1:
        role = "无"
    else:
        role = soup.find(class_="second-ul").contents[0].contents[1]
    # print(role)
    country = soup.find(class_="detail-info").contents[0].contents[2].contents[1]
    # print(country)
    if soup.find(class_="box_chart") is None:
        print(name + " " + country + " " + role)
        print("无能力值")
        print()
        if role!="门将":
            insertPlayer("球员", name, country, role, 'NULL', 'NULL', 'NULL', 'NULL',
                         'NULL', 'NULL')
        return None

    for box in soup.find(class_="box_chart").children:
        if not flag:
            flag = True
        else:
            if isinstance(box, bs4.element.Tag):
                cap = box.contents[0]
                num = box.contents[1].contents[0]
                capability[cap] = num
    print(name + " " + country + " " + role)
    print(capability)
    if role!="门将":
        insertPlayer("球员", name, country, role, capability["速度"], capability["力量"], capability["防守"], capability["盘带"],
           capability["传球"], capability["射门"])
    else:
        insertPlayer("球员", name, country, role, capability["扑救"], capability["位置"], capability["速度"], capability["反应"],
                     capability["开球"], capability["手型"])
    print()


if __name__ == '__main__':
    db_init()
    teamA = {"日本": "50001146", "澳大利亚": "50000087", "沙特阿拉伯": "50001640", "中国": "50000344", "阿曼": "50001390",
             "越南": "50002040"}
    country_dict = {}
    teamB = {"伊朗": "50000986", "韩国": "50001181", "阿联酋": "50001998", "伊拉克": "50000987", "叙利亚": "50001932",
             "黎巴嫩": "50001193"}
    # getPlayers(teamA["日本"], "日本")
    for key in teamA.keys():
        country_dict[key] = getPlayers(teamA[key], key)
    for key in teamB.keys():
        country_dict[key] = getPlayers(teamB[key], key)
    for key in country_dict.keys():
        for k in country_dict[key].keys():
            getCap(country_dict[key][k], k, key)

    print("succ")
