from app import app
import urllib.request,json
from .models import classes
Article = classes.Article
Source = classes.Source
News = classes.News

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]
source_url = app.config['NEWS_SOURCE_URL']
news_url = app.config['NEWS_ARTICLE_URL']

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt= article_item.get('publishedAt')

        if urlToImage and description:
            article_object = Article(title,description,url,urlToImage,publishedAt)
            article_results.append(article_object)

    return article_results

def get_sources(sources):
    get_source_url=source_url.format(sources,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        source_data=url.read()
        source_response=json.loads(source_data)

        source_results=None

        if source_response["sources"]:
            new_source_results=source_response["sources"]
            source_results=process_sources(new_source_results)
    return source_results

def process_sources(source_list):
    source_results=[]
    for source in source_list:
        id=source.get("id")
        name=source.get("name")
        description=source.get("description")
        url=source.get("url")

        source_object=Source(id,name,description,url)
        source_results.append(source_object)

    return source_results

def get_news(name):
    get_news_url=news_url.format(name,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        news_data=url.read()
        news_response=json.loads(news_data)

        news_object=None

        if news_response['articles']:
            news_result_list=news_response["articles"]
            news_results=process_news(news_result_list)
    return news_results


def process_news(news_list):
    news_results=[]
    for news in news_list:
        title=news.get("title")
        description=news.get("description")
        url=news.get("url")
        urlToImage=news.get("urlToImage")
        publishedAt=news.get("publishedAt")
        
        if urlToImage and description:
            news_object=News(title,description,url,urlToImage,publishedAt)
            news_results.append(news_object)

    return news_results 
