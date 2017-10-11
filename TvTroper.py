import sys
import requests
from bs4 import BeautifulSoup

searchLink = 'https://google.com/search?q=tvtropes+'
#gameFound = False
linkList = []
#while not gameFound :
gameFound = True
print('Enter the name of a Game, and similar games will be found: ')
sys.stdout.flush()

#inputText = raw_input()
inputText = "mario"
page = requests.get(searchLink + inputText)
#page = requests.get('http://tvtropes.org/pmwiki/pmwiki.php/Main/CouldntFindALighter')
contents = page.content
#print(contents)
soup = BeautifulSoup(contents, 'html.parser')
#linkList = soup.findAll("a", href=lambda href: href and "VideoGame" in href)
for link in soup.findAll('a') :
    if 1==1 :
        temp = link['href']
        temp.decode('utf-8')
        linkList.append(temp)
for i in linkList :
    print (i)
print(type(linkList[0]))
