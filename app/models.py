class Article:
    '''
    Article class to define article object
    '''
    def __init__(self,source,author,title,description,publishedAt,url,urlToImage,content):
        self.author =author
        self.title = title
        self.description = description
        self.url=url
        self.urlToImage=urlToImage
        self.content=content
        self.publishedAt=publishedAt

class Sources:
    def __init__(self,id, name,description,url):
        self.id=id
        self.name=name
        self.description=description
        self.url=url