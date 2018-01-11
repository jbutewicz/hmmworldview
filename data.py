# List of RSS feeds used to pull articles from
rss_feeds = {
    'ABC News' : 'http://abcnews.go.com/abcnews/topstories',
    'BBC News' : 'http://feeds.bbci.co.uk/news/rss.xml',
    'CBS News' : 'https://www.cbsnews.com/latest/rss/main',
    'CNN' : 'http://rss.cnn.com/rss/cnn_topstories.rss',
    'Daily Mail' : 'http://www.dailymail.co.uk/articles.rss',
    'Fox News' : 'http://feeds.foxnews.com/foxnews/latest',
    'Huffington Post' : 'https://www.huffingtonpost.com/section/front-page/feed',
    'Los Angeles Times' : 'http://www.latimes.com/rss2.0.xml',
    'MSN' : 'https://rss.msn.com/',
    'New York Daily News' : 'http://www.nydailynews.com/cmlink/NYDN.News.rss',
    'New York Post' : 'https://nypost.com/feed/',
    'Reuters' : 'http://feeds.reuters.com/reuters/topNews',
    'The New Yorker' : 'https://www.newyorker.com/feed/news',
    'The New York Times' : 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'The Wall Street Journal' : 'http://www.wsj.com/xml/rss/3_7085.xml',
    'Time' : 'http://feeds2.feedburner.com/time/topstories',
    'USA Today' : 'http://rssfeeds.usatoday.com/usatoday-NewsTopStories',
    'Washington Post' : 'http://feeds.washingtonpost.com/rss/world',
    'Yahoo News' : 'https://www.yahoo.com/news/rss'
}

# Number of articles to grab per each RSS feed
POSTS_FROM_EACH_FEED = 1
POSTS_FROM_EACH_FEED_KEYWORDS = 1

# Minimum image size kb allowed (used to control image quality and remove small images like logos)
MIN_IMAGE_SIZE = 30

# Final image size and width
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080

# Number of images to stack for our image
IMAGES_TO_STACK = 10
