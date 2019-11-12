from bs4 import BeautifulSoup
import requests

request1 = requests.get("https://en.wikipedia.org/wiki/New_York_State_Route_373")

soup = BeautifulSoup(request1.text, 'html.parser')
soup1 = (soup.find(id="bodyContent"))
for i in soup1.findAll('a'):
    listofextensions = [".jpg", ".svg"]
    testurl = i.get('href')
    if testurl[0:5] == "/wiki":
        if all(x not in testurl for x in listofextensions):
            print(testurl)
