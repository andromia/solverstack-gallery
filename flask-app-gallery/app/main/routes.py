from app import db, ROOT
from app.main import bp
from app.utils import url_for

from flask import render_template, flash, redirect, request, g, \
    jsonify, current_app, make_response
from json import load

import os


@bp.before_app_request
def before_request():
    pass

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')

def get_static_json(filename:str):
    """
    Reads filename from /static as json.

    :filename:      str of filename ('data.json')

    returns json.load() obj
    """
    json_path = os.path.join(ROOT, 'app', 'static', filename)
    data = load(open(json_path))

    return data

@bp.route('/vrp', methods=['GET', 'POST'])
def vrp():
    if request.method == 'GET':
        data = get_static_json('vrp_data.json')

    return render_template('vrp.html', data=data)