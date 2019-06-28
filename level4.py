import urllib.request
import re
 
# Initial nothing is 12345
firstnothing = "12345"
page= urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + firstnothing)
pageData = page.read().decode('utf-8')
nextNothing = re.findall('[0-9]+',pageData)
print(nextNothing)
while len(nextNothing) != 0 :
    lastNothing = nextNothing[0]
    page= urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nextNothing[0])
    pageData = page.read().decode('utf-8')
    nextNothing = re.findall('[0-9]+',pageData)
    print(nextNothing)
#second clue given is to divide by two and keep going. 
# so take the last nothing, divide, and go till its done. 
calcNothing = int(lastNothing)/2
page= urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(calcNothing))
pageData = page.read().decode('utf-8')
nextNothing = re.findall('[0-9]+',pageData)
while len(nextNothing) != 0 :
    lastNothing = nextNothing[0]
    page= urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nextNothing[0])
    pageData = page.read().decode('utf-8')
    nextNothing = re.findall('and the next nothing is ([0-9]+)',pageData)
    print(nextNothing)
print('The needed url is: ', pageData)