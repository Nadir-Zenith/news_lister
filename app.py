
from flask import Flask, render_template, request
from src.fetch_feeds import get_articles, paginate



app = Flask(__name__)


@app.route("/")
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    articles, sources = get_articles()

    paginated_articles = paginate(page, per_page, articles)

    return render_template('index.html', articles=paginated_articles,categories=sources,
                           page=page, total_pages=len(articles)//per_page + 1)

@app.route("/search")
def search():
    query = request.args.get('q')

    articles, sources = get_articles(query)

    return render_template('search_results.html', articles=articles, categories=sources,query=query)


@app.route("/filter")
def filter_items():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    selected_source = request.args.get('category', 'All')

    if selected_source == "All":
        articles, sources = get_articles()
    else:
        articles, sources = get_articles(source = selected_source)

    paginated_articles = paginate(page, per_page, articles)

    return render_template('index.html', articles=paginated_articles,categories=sources,
                           page=page, total_pages=len(articles)//per_page + 1)

if __name__ == "__main__":
    app.run(debug=True)