# Filename: common_utils.py

def load_data(file_path):
    # Load the set attributes_data from a JSON file
    set_attributes_data = load_set_attributes_data(set_data_path)

def load_set_attributes_data(set_data_path):
    with open(set_data_path, 'r', encoding='utf-8') as set_json_file:
        set_attributes_data = json.load(set_json_file)
    return set_attributes_data