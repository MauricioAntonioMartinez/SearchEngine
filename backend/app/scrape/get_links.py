
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


class Scraper:
    """Class to scrape in a given url and find all links to new pages"""

    def __init__(self,url):
        self.URL = url

    def find_links(self):
        try: 
            response = requests.get(self.URL)
            data = BeautifulSoup(response.text,"html.parser")
            head = data.find("head")
            host = "https://"+ urlparse(self.URL).netloc
            title=""  
            if head:  
                title=head.find("title").text
            anchor_tags = data.find_all("a")  
            body = data.find('body')  
            if not body: 
                body = ""
            content = body.get_text()
            links = {frozenset({a.get("href"),host}) for a in anchor_tags} 
            print(links)   
            print(host)   
            return links,content,title 
        except Exception as e:
            print(e)
            return None,None,None


