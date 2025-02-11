from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/services')
def services():
    return render_template('services.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')