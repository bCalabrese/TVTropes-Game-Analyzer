import sys 
import urllib.request #url library opener
import string #string operations
import re #regex
#import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


searchLink = 'https://google.com/search?gbv=1&q=tvtropes.org+'
#searchLink = 'http://tvtropes.org/pmwiki/search_result.php?q='
gameFound = False
while gameFound == False : #Loop input until user finds the game they were looking for
    linkList = []
    table1 = PrettyTable(['Number','Game Name'])
    print('Enter the name of a Game, and similar games will be found: ')
    sys.stdout.flush()

    inputText = input() #Get user input for game
    #inputText = "zelda 1"
    inputText = inputText.replace(' ','+') #Replace spaces with + for search
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(searchLink + inputText)
    soup = BeautifulSoup(page, 'html.parser')
    #linkList = soup.findAll("a", href=lambda href: href and "VideoGame" in href)
    for link in soup.findAll('a') :
        print(link['href'])
        if u'tvtropes' in link['href'] :
            temp = link['href']
            temp = temp[temp.find('http://tvtropes'):temp.find('&')+1]
            temp = temp[temp.find('http://tvtropes'):temp.find('%')]
            if 'videogame' in temp.lower() and temp not in linkList :
                linkList.append(temp)
    if len(linkList) == 0:
        print('No results found, try again')
        continue
    for i in range(len(linkList)) :
        #print(linkList[i][48:])
        temp = str(linkList[i][48:])
        temp = re.sub(r"(?<=\w)([1-9A-Z])", r" \1", temp)
        #print(type(temp))
        table1.add_row([(i+1),temp])
    print (table1)
    print ('Enter the number of the game you want, else input will be regotten')
    sys.stdout.flush()
    gameSelect = input()
    if (0 <= int(gameSelect)-1 <= len(linkList)-1) :
        gameLink = linkList[int(gameSelect)-1]
        print(gameLink)
        gameFound = True

