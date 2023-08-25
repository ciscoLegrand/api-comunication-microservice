import requests
import os
import app.utils.logger as logger

BASE_URL = os.getenv("PRODUCTION_URL")
TOKEN = os.getenv("TOKEN")
headers_get = {"Authorization": f"Bearer {TOKEN}"}

def fetch_attributes():
    try:
        url = f"{BASE_URL}/api/v2/attributes"  # Punto final de ejemplo
        response = requests.get(url, headers=headers_get)
        
        if response.status_code == 200:
            logger.log_info("🔵 Datos obtenidos correctamente de la API para atributos.")
            return response.json()
        else:
            logger.log_error(f"🔴 [fetch_attributes] Error al obtener los atributos de la API. Código de estado: {response.status_code}")
            return {"error": "Error al obtener los atributos."}
    except Exception as e:
        logger.log_error(f"🔴 [fetch_attributes] Error al obtener los atributos de la API: {str(e)}")
        return {"error": f"Error al obtener los atributos: {str(e)}"}

def list_all_attributes():
    attributes = fetch_attributes()
    if "error" not in attributes:
        logger.log_info(f"🔵 Listando todos los atributos: {attributes}")
        return attributes
    else:
        return attributes

def get_attribute_by_identifier(identifier):
    attributes = fetch_attributes()
    if "error" not in attributes:
        for attribute in attributes:
            if attribute.get("_id") == identifier or attribute.get("name") == identifier:
                logger.log_info(f"🔵 Atributo encontrado con el identificador {identifier}: {attribute}")
                return attribute
        logger.log_warning(f"🟠 No se encontró atributo con el identificador {identifier}")
        return {"error": f"No se encontró atributo con el identificador {identifier}"}
    else:
        return attributes

def get_attributes_count():
    attributes = fetch_attributes()
    if "error" not in attributes:
        count = len(attributes)
        logger.log_info(f"🔵 Número total de atributos: {count}")
        return count
    else:
        return attributes

def list_attribute_names():
    attributes = fetch_attributes()
    if "error" not in attributes:
        names = [attribute.get("name") for attribute in attributes]
        logger.log_info(f"🔵 Nombres de atributos: {names}")
        return names
    else:
        return attributes

# Otras funciones de servicio relacionadas con atributos pueden ser definidas de manera similar...
