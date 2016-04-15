from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api/<group_name>')


@bp.route('/create')
def create_group(group_name):
    return "group created: " + group_name
