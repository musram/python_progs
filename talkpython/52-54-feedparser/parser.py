import feedparser

FEED_FILE = "newreleases.xml"


if __name__ == "__main__":
    feed = feedparser.parse(FEED_FILE)

    print(feed)

    if 'title' in feed.entries[0]:
        for entry in feed.entries:
            print(entry.published + " - " + entry.title + ": " + entry.link)
