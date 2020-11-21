from flask import render_template
from app import app
from .request import get_articles

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

    # search_movie = request.args.get('movie_query')

    # if search_movie:
    #     return redirect(url_for('search',movie_name=search_movie))
    # else:
    #     return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )

    return render_template('index.html', title = title, science = science_news, entertainment = entertainment_news, general = general_news, technology = technology_news)