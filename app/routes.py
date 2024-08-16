"""
NOTE:
    -------------------
    Decorator patterns:
    -------------------
    A common pattern with decorators is to use them to register functions as callbacks for certain
    events.
"""

from app import app


@app.route("/")
@app.route("/index")
def index():
    return "Hello World!"
