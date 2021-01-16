import functools
from flask import Blueprint, request, render_template

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        search = request.form.get('search')
        print(search)
        pass
    return render_template('home.html')