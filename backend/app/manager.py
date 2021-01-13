import concurrent.futures

from metadata.get_data import MetadataStractor
from scrape.get_links import Scraper


# 4 threads
class SearchEngine:

    general_links={}

    def __init__(self,root,db):
        self.root= root
        self.db = db
    
    def index_page(self):
        links,content,title =  Scraper(self.root).find_links()
        if not links:
            return
        self.general_links = links
        metadata =  MetadataStractor(content).find_metadata()
        self.store_result(title,metadata,self.root)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures =[]
            for _ in range(10):
                futures.append(executor.submit(self.thread_executor))
            return [f.result() for f in futures]

            
            
    def thread_executor(self):
        while self.general_links:
            link,host = self.general_links.pop()
            if not str(link).startswith("http"):
                link= host + link
            links,content,title =  Scraper(link).find_links()
            if not links:
                continue
            self.general_links|=links
            metadata = MetadataStractor(content).find_metadata()
            self.store_result(title,metadata,link)
        return "Success"


    def store_result(self,title,metadata,link):
        self.db.write({"title":title,"metadata":metadata,"link":link})
    
