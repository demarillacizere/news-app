class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?pageSize=4&country=us&category={}&apiKey={}'
    NEWS_ARTICLE_URL="https://newsapi.org/v2/top-headlines?sources={}&apiKey={}" 
    NEWS_SOURCE_URL='https://newsapi.org/v2/{}?language=en&apiKey={}'   



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