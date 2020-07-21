from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app, make_response
from app import db
from app.main import bp


@bp.before_app_request
def before_request():
    pass

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')

@bp.route('/vrp', methods=['GET', 'POST'])
def vrp():
    if request.method == 'GET':
        pass

    return render_template('vrp.html', data=[])