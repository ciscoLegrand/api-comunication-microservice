from flask import jsonify
import app.utils.logger as logger
from app.services import answers_service
from app.handlers import error_handlers

def get_answers(enterprise_id):
    try:
        answers = answers_service.fetch_answers(enterprise_id)
        logger.log_info(f"🔵 Respuestas de enterprise {enterprise_id} obtenidas correctamente.")
        return jsonify(answers), 200
    except requests.RequestException as e:
        logger.log_error(f"🔴 Error al obtener respuestas de {enterprise_id}. Razón: {str(e)}")
        if e.response.status_code == 404:
            return error_handlers.handle_404_error(e)
        else:
            return error_handlers.handle_500_error(e)

