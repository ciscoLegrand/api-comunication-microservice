def format_enterprise_data(enterprise_list):
    """
    Format the list of enterprises to only show the required fields.
    """
    formatted_data = []
    for enterprise in enterprise_list:
        formatted_enterprise = {
            "_id": enterprise.get("_id", "No existe _id en la empresa"),
            "name": enterprise.get("name", "No existe name en la empresa"),
            "questions_on": enterprise.get("questions_on", "No existe questions_on en la empresa"),
            "subscribed": enterprise.get("subscribed", "No existe subscribed en la empresa")
        }
        formatted_data.append(formatted_enterprise)

    return formatted_data

