# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
import pandas as pd


@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html', segment='index')


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template(template, segment=segment)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


@blueprint.route('/state_result', methods=['GET', 'POST'])
def data():
    try:
        print("Hello world!")
        state_search = str(request.form['state'])

        data = pd.read_csv('disasterdata.csv')

        data = data[data['state'] == state_search]
        state = data['state'].tolist()
        flood = data['Flood'].tolist()
        tornado = data['Tornado'].tolist()
        hurricane = data['Hurricane'].tolist()
        wildf = data['wildf'].tolist()
        power_outage = data['Power Outage'].tolist()

        week = data['covid_7'].tolist()
        month = data['covid_1'].tolist()
        month2 = data['covid_2'].tolist()

        #
        if flood[0] == 1:
            fl = "YES"
        else:
            fl = "NO"

        if tornado[0] == 1:
            tor = "YES"
        else:
            tor = "NO"

        if hurricane[0] == 1:
            hur = "YES"
        else:
            hur = "NO"


        if power_outage[0] == 1:
            po = "YES"
        else:
            po = "NO"

        if wildf[0] == 1:
            wf = "YES"
        else:
            wf = "NO"

        print(fl, tor,hur)
        n_data ={'state':state[0],'week':week[0],'month':month[0],'month2':month2[0]}
        bol_data = { 'flood':fl,'hur':hur,'power':po,'torn':tor,'wildfire':wf}


        return render_template('safe-search-form.html',data ="TRUE",n_data = n_data,bol_data = bol_data )
    except:
        return render_template('safe-search-form.html',data ="FALSE" )