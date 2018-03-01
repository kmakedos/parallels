import requests
import re
import multiprocessing

class FileHandler(object):
    def __init__(self):
        self.urls = None
        self.href = re.compile('<a href=["|\']htt[p|ps]://(.*)/[\'|"](.*)>')
        self.url_list = []

    def geturls(self, url):
        myfile =  requests.get(url)
        myurls = []
        for line in myfile:
           res =  re.search(self.href, line)
           if res:
               myurls.append(res.group(1))
        return myurls

    def seturls(self, urls):
        self.urls = urls

    def start(self):
        for url in self.urls:
            self.url_list.append(self.geturls(url))

    def start_multiproc(self, workers):
        pool = multiprocessing.Pool(processes = workers)
        lists = pool.map_async(self.geturls, self.url_list)
        lists.wait()
        for listitem in lists
            self.url_list.append(listitem)


    def print_results(self):
        for k in self.url_list:
            print(k)