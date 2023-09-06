import os
import pandas as pd
import json

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Adjust the path to the JSON data files to go up one level and then to the data folder
set_data_path = os.path.join(current_dir, '..', 'data', 'pokemon-tcg-data', 'sets', 'en.json')
card_data_folder = os.path.join(current_dir, '..', 'data', 'pokemon-tcg-data', 'cards', 'en')

# Define the fields and attributes for the set data schema based on the columns in the DataFrames
set_schema = {
    'set_id': str,
    'set_name': str,
    'set_series': str,
    'set_printedTotal': int,
    'set_total': int,
    'set_legalities': {
        'set_standard': str,
        'set_expanded': str,
        'set_unlimited': str
    },
    'set_ptcgoCode': str,
    'set_releaseDate': str,
    'set_updatedAt': str,
    'set_images': {
        'set_symbol': str,
        'set_logo': str
    }
}

# Define the fields and attributes for the card data schema based on the columns in the DataFrames
card_schema = {
    'id': str,
    'name': str,
    'supertype': str,
    'subtypes': list,
    'hp': str,
    'types': list,
    'evolvesFrom': str,
    'evolvesTo': list,
    'rules_list': list,
    'ancientTrait': {
        'name': str,
        'text': str
    },
    'abilities': {
        'name': str,
        'text': str,
        'type': str
    },
    'attacks': {
        'name': str,
        'cost': str,
        'convertedEnergyCost': int,
        'damage': str,
        'text': str
    },
    'weaknesses': {
        'type': str,
        'value': str
    },
    'resistances': {
        'type': str,
        'value': str
    },
    'retreatCost': str,
    'convertedRetreatCost': int,
    'card_set': {
        'set_id': str,
        'set_name': str,
        'set_series': str,
        'set_printedTotal': int,
        'set_total': int,
        'set_legalities': {
            'set_standard': str,
            'set_expanded': str,
            'set_unlimited': str
        },
        'set_ptcgoCode': str,
        'set_releaseDate': str,
        'set_updatedAt': str,
        'set_images': {
            'set_symbol': str,
            'set_logo': str
        }
    },
    'number': str,
    'artist': str,
    'rarity': str,
    'flavorText': str,
    'nationalPokedexNumbers': list,
    'legalities': {
        'unlimited': str,
        'standard': str,
        'expanded': str
    },
    'regulationMark': str,
    'images': {
        'small': str,
        'large': str
    }
}

# Define a list of required fields based on your criteria
required_fields = ['id', 'name']

# Load the set attributes data from a JSON file with explicit encoding specification
with open(set_data_path, 'r', encoding='utf-8') as set_json_file:
    set_attributes_data = json.load(set_json_file)

# Create an empty DataFrame for card data based on the defined schema
card_df = pd.DataFrame(columns=card_schema.keys())

# Initialize an empty list to store valid card data
valid_card_data_list = []

# Iterate through JSON files in the card data folder
for filename in os.listdir(card_data_folder):
    if filename.endswith('.json'):
        card_attributes_json_path = os.path.join(card_data_folder, filename)

        # Load card attributes data from a JSON file
        with open(card_attributes_json_path, 'r', encoding='utf-8') as card_json_file:
            card_attributes_data = json.load(card_json_file)

        # Check if card_attributes_data is not None
        if card_attributes_data is not None:
            # Iterate over the loaded data and filter based on the schema
            for item in card_attributes_data:
                # Create a dictionary to store valid card data
                valid_card_data = {}

                for field, field_schema in card_schema.items():
                    if field != 'card_set':
                        if isinstance(field_schema, dict):
                            # If the field schema is a nested dictionary, iterate over its keys
                            if isinstance(item.get(field), dict):
                                valid_card_data[field] = {nested_field: item[field].get(nested_field) for nested_field in field_schema.keys()}
                            else:
                                valid_card_data[field] = {}  # Create an empty dictionary if the field is not a dictionary
                        else:
                            # If the field schema is not a dictionary, get the value directly
                            if isinstance(item.get(field), list):
                                valid_card_data[field] = item[field]  # Keep the list as is
                            else:
                                valid_card_data[field] = item.get(field)  # Get the value directly

                # Add set data from set_schema
                valid_card_data['card_set'] = set_schema

                # Append the valid card data to the list
                valid_card_data_list.append(valid_card_data)

# Create a DataFrame from the list of valid card data
card_df = pd.DataFrame(valid_card_data_list)

# Print the card DataFrame
print(card_df)
