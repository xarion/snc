from flask import Blueprint, jsonify

from model import Group

bp = Blueprint('api', __name__, url_prefix='/api/<group_name>')


@bp.route('/create')
def create_group(group_name):
    Group.create(group_name)
    resp = jsonify(status="OK", group_name=group_name)
    resp.status_code = 201
    return resp
