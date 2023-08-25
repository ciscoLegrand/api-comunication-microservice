from flask import Blueprint, request
from app.controllers import enterprises_controller

enterprises_bp = Blueprint('enterprises', __name__)

@enterprises_bp.route('/enterprises', methods=['GET'])
def get_all_enterprises():
    return enterprises_controller.get_enterprises()

@enterprises_bp.route('/enterprises/<string:enterprise_id>', methods=['GET'])
def get_single_enterprise_by_id(enterprise_id):
    return enterprises_controller.get_enterprise_by_id(enterprise_id)

@enterprises_bp.route('/enterprises/name/<string:name>', methods=['GET'])
def get_single_enterprise_by_name(name):
    return enterprises_controller.get_enterprise_by_name(name)
