import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?pageSize=4&country=us&category={}&apiKey=3530228c891345a787748c97ba00ac2a'
    NEWS_ARTICLE_URL="https://newsapi.org/v2/top-headlines?sources={}&apiKey=3530228c891345a787748c97ba00ac2a" 
    NEWS_SOURCE_URL='https://newsapi.org/v2/{}?language=en&apiKey=3530228c891345a787748c97ba00ac2a'  
    # NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
    # SECRET_KEY=os.environ.get("SECRET_KEY") 



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True