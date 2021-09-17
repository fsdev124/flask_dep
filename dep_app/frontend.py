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
from .dep import Device, Delivery, Order, bulk_enroll_devices
from random import randint

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
        try:
            os.environ['DEP_ENV'] = request.form['dep_env']
            os.environ['DEP_SHIPTO'] = request.form['dep_ship_to']
            os.environ['DEP_RESELLER_ID'] = request.form['dep_reseller_id']
            os.environ['DEP_UAT_CERT'] = request.form['dep_uat_cert']
            os.environ['DEP_UAT_PRIVATE_KEY'] = request.form['dep_uat_private_key']

            order_number = f"ORDER_{randint(10000000, 99999999)}"
            transaction_number = f"TXN_{randint(10000000, 99999999)}"
            delivery_number = f"D{randint(10000000, 99999999)}"
            order_date = datetime.utcnow()
            ship_date = datetime.strptime(request.form['ship_date'], '%Y-%m-%d')
            
            all_devices = []
            devices = request.form['devices'].split('\n')
            for device in devices:
                d = device.split(',')
                all_devices.append(Device(d[0], d[1]).json())

            # Create a list of Delivery objects and add Device objects' list
            deliveries = [Delivery(delivery_number, ship_date, all_devices).json()]

            # Create an Order object and add Delivery objects list
            order = Order(order_number, order_date, request.form['order_type'], request.form['customer_id'], None, deliveries).json()

            # Call the Bulk Enroll Devices endpoint with Order object
            post_data, res, error_code, error_message, call_type = bulk_enroll_devices(transaction_number, order)

            if error_code:
                return jsonify({'result': 'failed', 'value' : {'error_code': error_code, 'error_message': error_message}})
    
            if 'deviceEnrollmentTransactionId' in res:
                return jsonify({'result': 'success', 'value': res})
            else:
                return jsonify({'result': 'failed', 'value': res})

        except Exception as e:
            error_message = e.args[0]

    return jsonify({'result': 'invalid request', 'value' : {'error_message': error_message}})

@frontend.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for('.login'))