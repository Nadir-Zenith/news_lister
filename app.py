
from flask import Flask, render_template, request
from src.fetch_feeds import get_articles, paginate



app = Flask(__name__)


@app.route("/")
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    articles = get_articles()

    paginated_articales = paginate(page, per_page, articles)

    return render_template('index.html', articles=paginated_articales,
                           page=page, total_pages=len(articles)//per_page + 1)



@app.route("/search")
def search():
    query = request.args.get('q')

    articles = get_articles(query)

    return render_template('search_results.html', articles=articles, query=query)