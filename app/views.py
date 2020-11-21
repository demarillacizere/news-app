from flask import render_template
from app import app
from .request import get_articles,get_sources,get_news

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

    return render_template('index.html', title = title, science = science_news, entertainment = entertainment_news, general = general_news, technology = technology_news)

@app.route("/source/<name>")
def source(name):
    bbc=get_news("abc-news")
    abc=get_news("abc-news-au")
    aljezera=get_news("al-jazeera-english")
    technica=get_news("ars-technica")

    return render_template("source.html",name=name,bbc_news=bbc,abc_news=abc,aljezera_n=aljezera,tech=technica)
