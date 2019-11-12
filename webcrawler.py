from bs4 import BeautifulSoup
import requests
import random
import networkx as nx
import matplotlib.pyplot as plt

class UrlItem:

    """
    UrlItem class
    """

    def __init__(self, url: str, depth: int):
        self.url = url
        self.depth = depth

class Crawler:

    def __init__(self, maxdepth):
        self.maxdepth = maxdepth
        self.queue = []
        self.myset = set([])

    def crawl(self, my_url):

        firsturl = UrlItem(my_url, 0)
        self.queue.append(firsturl)

        while len(self.queue) > 0:
            item = self.queue[0]
            current_depth = item.depth
            print(item.url)
            new_urls = self.parser(item.url)
            del self.queue[0]

            print(len(new_urls))
            for url in new_urls:
                self.myset.add((item.url,url))
                newurl = UrlItem(url, current_depth + 1)
                if newurl.depth < self.maxdepth:
                    self.queue.append(newurl)

        return self.myset

    def parser(self, my_url):

        urlcount = 0
        my_url = "https://en.wikipedia.com" + my_url
        urllist = []
        request1 = requests.get(my_url)
        soup = BeautifulSoup(request1.text, 'html.parser')
        mainbody = soup.find(id="bodyContent")

        for link in mainbody.findAll('a'):
            if urlcount <= 2:
                testurl = link.get('href')
                testurl = self.checklink(testurl)
                if testurl:
                    urllist.append(testurl)
                    urlcount += 1
        return urllist

    def checklink(self, testurl):
        listofexclusions = [".png",".jpg", ".svg", "Help", "Template", "Category", "Special", "Citing"]
        if testurl and testurl[0:5] == "/wiki":
            if all(x not in testurl for x in listofexclusions):
                return testurl
        return None

    def creategraph(self, first_url):
        G = nx.DiGraph()
        for i in my_set:
            G.add_edge(i[0], i[1])
        print(G.edges())
        nx.draw(G, with_labels = False)
        plt.savefig("simple_path.png") # save as png
        plt.show() # display

if __name__ == "__main__":

    my_url = "/wiki/New_York_State_Route_373"
    maxdepth = 4
    my_crawl = Crawler(maxdepth)
    my_set = my_crawl.crawl(my_url)
    my_crawl.creategraph(my_url)








