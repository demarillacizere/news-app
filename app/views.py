from flask import render_template
from app import app
from .request import get_articles, get_sources,get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    science_news = get_articles('science')
    entertainment_news = get_articles('entertainment')
    general_news = get_articles('general')
    technology_news = get_articles('technology')
    title = 'Home - Browse news articles from all around the world'
    source = get_sources("sources")
    return render_template('index.html', title = title, science = science_news, entertainment = entertainment_news, general = general_news, technology = technology_news, sources=source)

@app.route("/source/<name>")
def body(name):
    news=get_news(name)

    return render_template("source.html",name=name, news=news)
