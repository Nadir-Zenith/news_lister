import feedparser
from src.rss_links import RSS_FEEDS, RSS_FEEDS_AI


def get_articles(query: str | None = None):
    articles = []

    for source, feed in RSS_FEEDS_AI.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    articles = sorted(articles, key = lambda x: x[1].published_parsed, reverse=True) 
    
    if query:
        results = [article for article in articles if query.lower() in article[1].title.lower()]
        return results
    
    return articles



def paginate(page:int, per_page:int, articles:list):
    total_articles = len(articles)
    start = (page-1) * per_page
    end = start + per_page
    return articles[start:end]