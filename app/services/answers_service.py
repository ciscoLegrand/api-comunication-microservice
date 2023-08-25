import os
import requests
from app.utils.answers import answers_data_formatter as formatter
import app.utils.logger as logger

BASE_URL = os.environ.get("PRODUCTION_URL")
TOKEN = os.environ.get("TOKEN")
HEADERS = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {TOKEN}"
}

def fetch_answers(enterprise_id):
    try:
        url = f"{BASE_URL}/api/v2/enterprises/{enterprise_id}/answers"
        response = requests.get(url, headers=HEADERS)
        
        response.raise_for_status()  # Esto levantará una excepción HTTP si el código de estado es 4xx o 5xx
        
        answers = response.json()
        return formatter.format_answer_data(answers)
    except requests.RequestException as e:
        logger.log_error(f"🔴 Error al realizar la petición: {str(e)}")
        raise e
