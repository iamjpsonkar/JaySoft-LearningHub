from flask import Flask
from urls import URLS
from logging import getLogger


app = Flask(__name__)
logger = getLogger()

for url in URLS:
    app.add_url_rule(rule=url[0],view_func=url[1],methods=url[2])

if __name__ == '__main__':
    logger.info("Starting App")
    app.run(debug=True)