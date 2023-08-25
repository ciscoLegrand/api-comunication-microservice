def list_to_dict(attributes_list):
    """
    Convert the list of attributes to a dictionary where the keys are the _ids and the values are the full attributes.
    """
    return {attribute["_id"]: attribute for attribute in attributes_list}

def get_attributes_by_type(attributes_list, attribute_type):
    """
    Return all attributes of a specific type.
    """
    return [attribute for attribute in attributes_list if attribute["type"] == attribute_type]

def format_for_display(attributes_list):
    """
    Prepare the attributes data for a more user-friendly display.
    """
    formatted_data = []
    for attribute in attributes_list:
        formatted_attribute = attribute.copy()
        if not formatted_attribute["description"]:
            formatted_attribute["description"] = "No description available."
        formatted_data.append(formatted_attribute)
    return formatted_data
