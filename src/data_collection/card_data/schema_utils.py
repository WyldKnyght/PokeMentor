# Filename: schema_utils.py

import os
import json
import pandas as pd
from pathlib import Path
from common_utils import load_set_attributes_data
from create_pandas_schema import load_set_attributes_data

# Import the load_set_attributes_data function from create_pandas_schema.py
from create_pandas_schema import load_set_attributes_data

# Get the current directory using pathlib
current_dir = Path(__file__).parent

# Define the project root directory (two levels up from the current script's directory)
project_root = current_dir.parent.parent  # Adjusted to move up two levels

# Corrected file path for set_data_path
set_data_path = project_root / 'data' / 'pokemon-tcg-data' / 'sets' / 'en.json'

# Call the function with the corrected path
set_attributes_data = load_set_attributes_data(set_data_path)

def get_set_schema(current_dir):
    # Update the path to the JSON data files using pathlib
    # Get the current script's directory
    current_dir = Path(__file__).resolve().parent

    return {
        # Define your set schema here
        'set_id': str,
        'set_name': str,
        'set_series': str,
        'set_printedTotal': int,
        'set_total': int,
        'set_legalities': {
            'set_standard': str,
            'set_expanded': str,
            'set_unlimited': str,
        },
        'set_ptcgoCode': str,
        'set_releaseDate': str,
        'set_updatedAt': str,
        'set_images': {'set_symbol': str, 'set_logo': str},
    }

def get_card_schema(current_dir):
    return {
        # Define your card schema here
        'id': str,
        'name': str,
        'supertype': str,
        'subtypes': list,
        'hp': str,
        'types': list,
        'evolvesFrom': str,
        'evolvesTo': list,
        'rules_list': list,
        'ancientTrait': {'name': str, 'text': str},
        'abilities': {'name': str, 'text': str, 'type': str},
        'attacks': {
            'name': str,
            'cost': str,
            'convertedEnergyCost': int,
            'damage': str,
            'text': str,
        },
        'weaknesses': {'type': str, 'value': str},
        'resistances': {'type': str, 'value': str},
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
                'set_unlimited': str,
            },
            'set_ptcgoCode': str,
            'set_releaseDate': str,
            'set_updatedAt': str,
            'set_images': {'set_symbol': str, 'set_logo': str},
        },
        'number': str,
        'artist': str,
        'rarity': str,
        'flavorText': str,
        'nationalPokedexNumbers': list,
        'legalities': {'unlimited': str, 'standard': str, 'expanded': str},
        'regulationMark': str,
        'images': {'small': str, 'large': str},
    }

# Get the current directory using pathlib
current_dir = Path(__file__).parent

# Corrected file path for set_data_path
set_data_path = project_root / 'data' / 'pokemon-tcg-data' / 'sets' / 'en.json'

# Call the function with the corrected path
set_attributes_data = load_set_attributes_data(set_data_path)

def create_empty_card_dataframe(card_schema):
    return pd.DataFrame(columns=card_schema.keys())

def extract_valid_card_data(card_schema, set_schema, card_attributes_data):
    valid_card_data_list = []

    for item in card_attributes_data:
        valid_card_data = {}

        for field, field_schema in card_schema.items():
            if field != 'card_set':
                if isinstance(field_schema, dict):
                    valid_card_data[field] = {
                        nested_field: item[field].get(nested_field)
                        for nested_field in field_schema.keys()
                    } if isinstance(item.get(field), dict) else {}
                else:
                    valid_card_data[field] = (
                        item[field] if isinstance(item.get(field), list) else item.get(field)
                    )

        valid_card_data['card_set'] = set_schema
        valid_card_data_list.append(valid_card_data)

    return valid_card_data_list
