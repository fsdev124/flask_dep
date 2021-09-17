# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, session
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask import current_app as app
from markupsafe import escape
from .models import SignupForm
from .nav import nav
import json, time, math, re, csv, os
from datetime import datetime, timedelta
import requests

frontend = Blueprint("frontend", __name__)

def stringToTime(string):
    return int(time.mktime(datetime.strptime(string, "%Y-%m-%d").timetuple()))

@frontend.route("/")
def index():
    if not 'username' in session:
        return redirect(url_for('.login'))
    
    return render_template("index.html")

@frontend.route("/login", methods=('GET', 'POST'))
def login():
    if 'username' in session:
        return redirect(url_for('.index'))
    error_msg = ''
    form = SignupForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        if (username == "admin" and password == "admin"):
            session['username'] = username

            return redirect(url_for('.index'))

    return render_template('login.html', form=form, error_msg=error_msg)

@frontend.route("/enroll", methods=['POST'])
def enroll():
    if 'username' in session:
        username = request.form['username']
        return jsonify({'result': 'success'})

    return jsonify({'result': 'invalid request'})

@frontend.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for('.login'))
