import feedparser
from src.rss_links import RSS_FEEDS, RSS_FEEDS_AI


def get_articles(query: str | None = None, source : str = "All"):
    articles = []
    
    for site, feed in RSS_FEEDS_AI.items():
        if source != "All":
            selected_feed = RSS_FEEDS_AI.get(source)
            print(f'{selected_feed=}')
            parsed_feed = feedparser.parse(selected_feed)
            entries = [(source, entry) for entry in parsed_feed.entries]
            articles.extend(entries)
            break
        parsed_feed = feedparser.parse(feed)
        entries = [(site, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    articles = sorted(articles, key = lambda x: x[1].published_parsed, reverse=True) 
    
    if query:
        results = [article for article in articles if query.lower() in article[1].title.lower()]
        return results
    
    return articles, list(RSS_FEEDS_AI.keys())



def paginate(page:int, per_page:int, articles:list):
    total_articles = len(articles)
    start = (page-1) * per_page
    end = start + per_page
    return articles[start:end]