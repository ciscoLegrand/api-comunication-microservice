from flask import jsonify
import app.utils.logger as logger
from app.services import enterprises_service

def get_enterprises():
    try:
        enterprises = enterprises_service.fetch_enterprises()
        return jsonify(enterprises), 200
    except Exception as e:
        logger.log_error(f"🔴 [ERROR] Failed to fetch enterprises. Reason: {str(e)}")
        return jsonify({"error": "Failed to fetch enterprises."}), 500

def get_enterprise_by_id(enterprise_id):
    enterprise = enterprises_service.get_enterprise_by_id(enterprise_id)
    if enterprise:
        return jsonify(enterprise), 200
    else:
        logger.log_warning(f"🟠 No se encontró empresa con el ID {enterprise_id}")
        return jsonify({"error": f"No se encontró empresa con el ID {enterprise_id}"}), 404

def get_enterprise_by_name(name):
    enterprise = enterprises_service.get_enterprise_by_name(name)
    if enterprise:
        return jsonify(enterprise), 200
    else:
        logger.log_warning(f"🟠 No se encontró empresa con el nombre {name}")
        return jsonify({"error": f"No se encontró empresa con el nombre {name}"}), 404
