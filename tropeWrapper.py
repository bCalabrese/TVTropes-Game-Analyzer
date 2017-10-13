import urllib.request #url library opener
import re #regex
import string
import time
import operator
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def getLinkList(link):
    linkList = []
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(link)
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.findAll('a') :
        if u'tvtropes' in link['href'] :
            temp = link['href']
            temp = temp[temp.find('http://tvtropes'):temp.find('&')+1]
            temp = temp[temp.find('http://tvtropes'):temp.find('%')]
            if '.php/videogame' in temp.lower() and temp not in linkList :
                linkList.append(temp)
    printTable(linkList)
    return linkList

def printTable(linkList):
    table1 = PrettyTable(['Number','Game Name'])    
    for i in range(len(linkList)) :
        temp = str(linkList[i][48:])
        temp = re.sub(r"(?<=\w)([1-9A-Z])", r" \1", temp)
        table1.add_row([(i+1),temp])
    print (table1)
    
def printTable2(gameList):
    table1 = PrettyTable(['Number','Game Name'])
    j = 1
    for i in gameList :
        temp = i[0]
        temp = re.sub(r"(?<=\w)([1-9A-Z])", r" \1", temp)
        table1.add_row([(j),temp])
        if j == 10 :
            break
        j+=1
    print (table1)
    
def getTropeList(gameLink):
    tropeList = []
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(gameLink)
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.findAll('a') :
        if 'tvtropes.org' in link['href'] and 'homepage' not in link['href'] : 
            temp = link['href']
            if '.php/main' in temp.lower() and temp not in tropeList :
                    tropeList.append(temp)
    return tropeList

def getGameDict(tropeList,gameName):
    gameDict = {}
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    for i in tropeList:
        page = opener.open(i)
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.findAll('a',href=True) :
            print(link['href'])
            if 'tvtropes.org' in link['href'] and 'homepage' not in link['href'] :
                temp = link['href']
                if '.php/videogame' in temp.lower() and gameName not in temp :
                    if temp[48:] in gameDict :
                        gameDict[temp[48:]] += 1
                    else :
                        gameDict[temp[48:]] = 1
        time.sleep(0.5)
    sortedDict = sorted(gameDict.items(), key=operator.itemgetter(1), reverse=True)
    #for i in sortedDict :
    #    print(i[0])
    printTable2(sortedDict)
    return sortedDict
