from flask import Flask, render_template
import feedparser

app = Flask(__name__)

# Define a route to display all top headlines
@app.route('/')
def all_top_headlines():
    bbc_url = "http://feeds.bbci.co.uk/news/rss.xml"
    nyt_url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    ft_url = "https://www.ft.com/?format=rss"
    economist_url = "https://www.economist.com/latest/rss.xml"
    fp_url = "https://foreignpolicy.com/feed/"
    hn_url = "https://news.ycombinator.com/rss"
    politico_url = "https://rss.politico.com/politics-news.xml"
    techcrunch_url = "https://techcrunch.com/feed/"
    bbc_feed = feedparser.parse(bbc_url)
    nyt_feed = feedparser.parse(nyt_url)
    ft_feed = feedparser.parse(ft_url)
    economist_feed = feedparser.parse(economist_url)
    fp_feed = feedparser.parse(fp_url)
    hn_feed = feedparser.parse(hn_url)
    politico_feed = feedparser.parse(politico_url)
    techcrunch_feed = feedparser.parse(techcrunch_url)
    bbc_headlines = bbc_feed.entries[:5]
    nyt_headlines = nyt_feed.entries[:5]
    ft_headlines = ft_feed.entries[:5]
    economist_headlines = economist_feed.entries[:5]
    fp_headlines = fp_feed.entries[:5]
    hn_headlines = hn_feed.entries[:5]
    politico_headlines = politico_feed.entries[:5]
    techcrunch_headlines = techcrunch_feed.entries[:5]
    return render_template('index.html', title='All Top Headlines', bbc_headlines=bbc_headlines, nyt_headlines=nyt_headlines, ft_headlines=ft_headlines, economist_headlines=economist_headlines, fp_headlines=fp_headlines, hn_headlines=hn_headlines, politico_headlines=politico_headlines, techcrunch_headlines=techcrunch_headlines)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
