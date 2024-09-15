"""
NOTE:
    The Flask application instance called "app" is imported from the package, also called "app"
"""

import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Activity


@app.shell_context_processor
def make_shell_context():
    return {"sa": sa, "so": so, "db": db, "User": User, "Activity": Activity}
