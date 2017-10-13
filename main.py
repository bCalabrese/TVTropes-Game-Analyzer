from tropeWrapper import getLinkList
from tropeWrapper import getTropeList
from tropeWrapper import getGameDict
import string #string operations


searchLink = 'https://google.com/search?gbv=1&q=tvtropes.org+'
#searchLink = 'http://tvtropes.org/pmwiki/search_result.php?q='
gameFound = False
while gameFound == False : #Loop input until user finds the game they were looking for
    print('Enter the name of a Game, and similar games will be found: ')
    inputText = input() #Get user input for game
    #inputText = "zelda 1"
    inputText = inputText.replace(' ','+') #Replace spaces with + for search
    linkList = getLinkList(searchLink+inputText)
    if len(linkList) == 0:
        print('No results found, try again')
        continue
    print ('Enter the number of the game you want, anything else to re-input')
    gameSelect = input()
    if (0 <= int(gameSelect)-1 <= len(linkList)-1) :
        gameLink = linkList[int(gameSelect)-1]
        print(gameLink)
        gameFound = True

tropeList = getTropeList(gameLink)
gameList = getGameDict(tropeList,gameLink[48:])
for i in gameList:
    print(i)
