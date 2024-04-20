from flask import Flask
from flask import stream_template

import article
import feed


app = Flask(__name__)


@app.route("/")
def webserver():
    feed_items = feed.fetch_items()
    articles = [article.new(feed_item) for feed_item in feed_items]
    return stream_template("hauptstadt.html", articles=articles)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=80)
