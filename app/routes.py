"""
NOTE:
    -------------------
    Decorator patterns:
    -------------------
    A common pattern with decorators is to use them to register functions as callbacks for certain
    events.

    -------------------
    Templates in Flask:
    -------------------
    Templates help achieve a separation between presentation and business logic. In Flask, templates
    are written as separate files, stored in a templates folder that is inside the application package.
    The render_template() function invokes the Jinja template engine that comes bundled with the Flask framework.
"""

from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Arthur"}
    schedules = [
        {
            "author": {"username": "John"},
            "activities": [{"name": "running", "start": "200020", "end": "203000"}],
            "expenses": [{"date": "2021-01-01", "amount": 100, "description": "shoes"}],
        }
    ]
    return render_template("index.html", title="Home", user=user, schedules=schedules)
