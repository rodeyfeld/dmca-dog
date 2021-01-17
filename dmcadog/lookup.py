import functools
from flask import Blueprint, request, render_template

bp = Blueprint('lookup', __name__, url_prefix='/')


@bp.route('/lookup/', methods=('POST', 'GET'))
def lookup():
    if request.method == 'POST':
        print(request.json['query'])
        pass
    return render_template('lookup.html')