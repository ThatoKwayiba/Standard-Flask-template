from . import Home_Blueprint
from flask import render_template
from ..extensions import db


@Home_Blueprint.route('/', methods=['POST', 'GET'])
def index():
    context = {
        "title": "Title",
    }
    return render_template("Home/index.html", **context)


