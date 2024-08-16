"""
NOTE:
    --------------------------
    Defining a starting point:
    -------------------------- 
    The __name__ variable is a Python predefined variable, which is set to the name of the module
    in which it is used. It is a starting point for Flask to know where to look for templates, static
    files, and so on. 
    
    -----------------------------------------
    The "app" package vs. the "app" variable:
    -----------------------------------------
    The app package is defined by the app directory and the __init__.py file, and
    is used to import the app variable. The app variable is an instance of the Flask class.

    ------------------
    The bottom import:
    ------------------
    The routes module is imported at the bottom and not at the top of the script as it is always done.
    The bottom import is a workaround to circular imports, a common problem in Flask applications.

"""

from flask import Flask

app = Flask(__name__)

from app import routes
