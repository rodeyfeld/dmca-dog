from .lumen_api import LumenAPI
from flask import Blueprint, request, render_template
bp = Blueprint('lookup', __name__, url_prefix='/')

api = LumenAPI()


@bp.route('/lookup', methods=('POST', 'GET'))
def lookup():

    if request.method == 'POST':
        data = request.get_json()
        total = api.process(data)
        return total
    return None
