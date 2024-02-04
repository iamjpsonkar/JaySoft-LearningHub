from flask import render_template
from flask.views import MethodView
from logger import getLogger

logger = getLogger()

class Home(MethodView):
    def get(self):
        logger.info("GET request for Home")
        return render_template('home.html')