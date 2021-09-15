# Welcome to the Flask-Bootstrap sample application. This will give you a
# guided tour around creating an application using Flask-Bootstrap.
#
# To run this application yourself, please install its requirements first:
#
#   $ pip install -r ./requirements.txt
#
# Then, you can actually run the application.
#
#   $ flask --app=dep_app dev
#
# Afterwards, point your browser to http://localhost:5000, then check out the
# source.

from flask import Flask
#from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap

from .frontend import frontend
from .nav import nav
from .config import SECRET_KEY
import os

def create_app(configfile=None):
    app = Flask(__name__)
    app.config.update(
        TESTING=True,
        SECRET_KEY=SECRET_KEY
    )
    #AppConfig(app)

    Bootstrap(app)

    app.register_blueprint(frontend)
    app.jinja_env.auto_reload = True
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    EXPORT_FOLDER = os.path.join(APP_ROOT, 'static', 'export')
    app.config['EXPORT_FOLDER'] = EXPORT_FOLDER

    nav.init_app(app)
    return app
