from flask import jsonify, request
import app.utils.logger as logger
from app.services import attributes_service
from app.utils.attributes import attribute_data_formatter as formatter

def get_attributes():
    try:
        attributes = attributes_service.list_all_attributes()
        formatted_attributes = formatter.format_for_display(attributes)
        return jsonify(formatted_attributes), 200
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] Failed to fetch attributes. Reason: {str(e)}")
        return jsonify({"error": "Failed to fetch attributes."}), 500

def get_attribute_by_identifier(identifier):
    try:
        attribute = attributes_service.get_attribute_by_identifier(identifier)
        if "error" in attribute:
            logger.log_warning(f"🟠 [WARNING] {attribute['error']}")
            return jsonify(attribute), 404
        return jsonify(attribute), 200
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] Failed to fetch attribute by identifier. Reason: {str(e)}")
        return jsonify({"error": f"Failed to fetch attribute with identifier {identifier}."}), 500
    
    

def get_attributes_count():
    try:
        count = attributes_service.get_attributes_count()
        return jsonify({"count": count}), 200
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] Failed to get attributes count. Reason: {str(e)}")
        return jsonify({"error": "Failed to get attributes count."}), 500

def list_attribute_names():
    try:
        names = attributes_service.list_attribute_names()
        return jsonify({"names": names}), 200
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] Failed to list attribute names. Reason: {str(e)}")
        return jsonify({"error": "Failed to list attribute names."}), 500
