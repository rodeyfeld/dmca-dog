import functools
from flask import Blueprint, request, render_template

bp = Blueprint('lookup', __name__, url_prefix='/')


@bp.route('/lookup', methods=('GET', 'POST'))
def lookup():
    if request.method == 'POST':
        # TODO: Process frontend input
        pass
    return render_template('lookup.html')