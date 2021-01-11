import functools
from flask import Blueprint, request, render_template

bp = Blueprint('dog', __name__, url_prefix='/dog')


@bp.route('/lookup', methods=('GET', 'POST'))
def dog():
    if request.method == 'POST':
        # TODO: Process frontend input
        pass
    return render_template('lookup.html')