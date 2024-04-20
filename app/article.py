import datetime as dt
import os
import urllib.parse


def new(article):
    path = urllib.parse.urlparse(article["url"])
    elements = os.path.split(path.path)
    url = "https://www.hauptstadt.be/a/" + "/".join(elements[1:])

    published = dt.datetime.strptime(article["published"], "%Y-%m-%dT%H:%M:%S.%fZ")
    publish_date = published.strftime("%d.%m.%Y")

    return {
        "title": article["title"],
        "description": article["summary"],
        "url": url,
        "publish_date": publish_date,
    }
