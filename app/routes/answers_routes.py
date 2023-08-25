from flask import Blueprint, request
from app.controllers import answers_controller

answers_bp = Blueprint('answers', __name__)

@answers_bp.route('/answers/<string:enterprise_id>', methods=['GET'])
def get_all_answers(enterprise_id):
    return answers_controller.get_answers(enterprise_id)
