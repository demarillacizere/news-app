class Article:
    '''
    Article class to define article object
    '''
    def __init__(self,title,description,url,urlToImage,publishedAt):
        self.title = title
        self.description = description
        self.urlToImage=urlToImage
        self.url=url
        self.publishedAt=publishedAt

class Source:
    def __init__(self,id, name,description,url):
        self.id=id
        self.name=name
        self.description=description
        self.url=url