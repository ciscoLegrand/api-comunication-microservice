import os
import requests
from app.utils.logger import log_info, log_error, log_warning
from app.utils.enterprises import enterprise_data_formatter as formatter

BASE_URL = os.environ.get("PRODUCTION_URL")
TOKEN = os.environ.get("TOKEN")
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"  # Corrección de la interpolación de cadena
}

def fetch_enterprises():
    url = f"{BASE_URL}/api/v2/enterprises"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        enterprises = response.json()
        
        if not isinstance(enterprises, list):
            log_error("🔴 [ERROR] La respuesta de la API no es una lista.")
            return []

        log_info(f"🔵 [INFO] Se obtuvieron {len(enterprises)} empresas de la API.")
        return formatter.format_enterprise_data(enterprises)

    except requests.RequestException as e:
        log_error(f"🔴 [ERROR] Error al hacer la solicitud a la API: {str(e)}")
        return []

def get_enterprise_by_id(enterprise_id):
    enterprises = fetch_enterprises()
    for enterprise in enterprises:
        if enterprise["_id"] == enterprise_id:
            log_info(f"🔵 [INFO] Empresa encontrada con ID {enterprise_id}.")
            return formatter.format_enterprise_data([enterprise])
    
    log_warning(f"🟠 [WARNING] No se encontró empresa con ID {enterprise_id}.")
    return None

def get_enterprise_by_name(name):
    enterprises = fetch_enterprises()
    for enterprise in enterprises:
        if enterprise["name"].lower() == name.lower():
            log_info(f"🔵 [INFO] Empresa encontrada con nombre {name}.")
            return formatter.format_enterprise_data([enterprise])
    
    log_warning(f"🟠 [WARNING] No se encontró empresa con nombre {name}.")
    return None
