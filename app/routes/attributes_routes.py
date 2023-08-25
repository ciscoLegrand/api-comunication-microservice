from flask import Blueprint, jsonify
from app.controllers import attributes_controller
import app.utils.logger as logger

attributes_bp = Blueprint('attributes', __name__)

@attributes_bp.route('/attributes', methods=['GET'])
def get_attributes():
    try:
        response, status = attributes_controller.get_attributes()
        logger.log_info(f"🔵 [INFO] attributes_routes Endpoint /attributes returned status code {status}")
        return response, status
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] attributes_routes Error at /attributes endpoint. Reason: {str(e)}")
        return jsonify({"error": "Failed to process request at /attributes endpoint."}), 500

@attributes_bp.route('/attributes/<identifier>', methods=['GET'])
def get_attribute_by_identifier(identifier):
    try:
        response, status = attributes_controller.get_attribute_by_identifier(identifier)
        logger.log_info(f"🔵 [INFO] attributes_routes Endpoint /attributes/{identifier} returned status code {status}")
        return response, status
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] attributes_routes Error at /attributes/{identifier} endpoint. Reason: {str(e)}")
        return jsonify({"error": f"Failed to process request at /attributes/{identifier} endpoint."}), 500

@attributes_bp.route('/attributes/count', methods=['GET'])
def get_attributes_count():
    try:
        response, status = attributes_controller.get_attributes_count()
        logger.log_info(f"🔵 [INFO] attributes_routes Endpoint /attributes/count returned status code {status}")
        return response, status
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] attributes_routes Error at /attributes/count endpoint. Reason: {str(e)}")
        return jsonify({"error": f"Failed to process request at /attributes/count endpoint."}), 500

@attributes_bp.route('/attributes/names', methods=['GET'])
def list_attribute_names():
    try:
        response, status = attributes_controller.list_attribute_names()
        logger.log_info(f"🔵 [INFO] attributes_routes Endpoint /attributes/names returned status code {status}")
        return response, status
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] attributes_routes Error at /attributes/names endpoint. Reason: {str(e)}")
        return jsonify({"error": f"Failed to process request at /attributes/names endpoint."}), 500
