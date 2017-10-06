from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup
import os
import sys

PATH = "E:\HD\Friends.S01-S10.720p.BluRay.x264-Tby"


def getPath(season, episode):
    folders = []
    files = []
    for entry in os.scandir(PATH):
        if entry.is_dir():
            folders.append(entry.path)
        elif entry.is_file():
            files.append(entry.path)

    for folder in folders:
        if folder.find(season) != -1:
            for root,dirs,files in os.walk(folder):
                for file in files:
                    if file.find(episode) != -1:
                        return (os.path.join(root, file))


for season in range(1,11):
    print("downloading Season: "+ str(season))
    URL = 'http://www.imdb.com/title/tt0108778/episodes?season=' + str(season)
    browser = mechanicalsoup.Browser()
    #proxies = {'http':'http://xxx.xxx.xxx.xx:xx'}
    #search_page = browser.get(URL, proxies=proxies)
    search_page = browser.get(URL)

    episodes = search_page.soup.find_all("div", itemprop="episodes")
    for episode in episodes:
        ep = str(episode.find('a')['href']).partition('_ep')[2]
        title = str(episode.find('a').contents[0])
        filePath =  os.path.split(getPath(".S" + str(season).zfill(2)  + ".", "e" + str(ep).zfill(2) ))
        newName = "s" + str(season).zfill(2) + ".e" + str(ep).zfill(2) + "."+ title +".mkv"
        newName = newName.replace(":",".")
        print('rename file: '+ os.path.join(filePath[0], filePath[1]) +' with: '+ os.path.join(filePath[0], newName))
        answer = str(input("Is the information correct? Enter Y for yes or N for no"))
        if answer == "y" or answer == "Y":
            os.rename(os.path.join(filePath[0], filePath[1]), os.path.join(filePath[0], newName))
        else:
            exit()
            
