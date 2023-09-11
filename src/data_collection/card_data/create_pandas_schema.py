# Filename create_pandas_schema.py

import sys
from pathlib import Path
import pandas as pd
import json
from common_utils import load_data
from schema_utils import get_set_schema, get_card_schema, create_empty_card_dataframe

# Get the current script's directory
current_dir = Path(__file__).resolve().parent

# Get the project root directory (two levels up from the current script's directory)
project_root = current_dir.parent.parent

# Add the project root directory to the Python path
sys.path.append(str(project_root))

# Import schema-related functions using absolute import
from schema_utils import get_set_schema, get_card_schema, load_set_attributes_data, create_empty_card_dataframe

# Adjust the path to the JSON data files using pathlib
set_data_path = project_root / 'data' / 'pokemon-tcg-data' / 'sets' / 'en.json'

# Corrected path to the card data folder
card_data_folder = project_root / 'data' / 'pokemon-tcg-data' / 'cards' / 'en'

# Load set schema and card schema using functions from schema_utils.py
set_schema = get_set_schema(current_dir)
card_schema = get_card_schema(current_dir)

# Create an empty DataFrame for card data based on the card schema
card_df = create_empty_card_dataframe(card_schema)

# Initialize an empty list to store valid card data
valid_card_data_list = []

def load_set_attributes_data(set_data_path):
    with open(set_data_path, 'r', encoding='utf-8') as set_json_file:
        set_attributes_data = json.load(set_json_file)
    return set_attributes_data

# Iterate through JSON files in the card data folder
for entry in card_data_folder.iterdir():
    if entry.name.endswith('.json') and entry.is_file():
        card_attributes_json_path = entry

        # Load card attributes data from a JSON file
        with open(card_attributes_json_path, 'r', encoding='utf-8') as card_json_file:
            card_attributes_data = json.load(card_json_file)

        # Check if card_attributes_data is not None
        if card_attributes_data is not None:
            # Use pandas.json_normalize() to extract valid card data
            valid_card_data_list.append(pd.json_normalize(card_attributes_data))

# Concatenate the list of DataFrames into a single DataFrame
valid_card_data_df = pd.concat(valid_card_data_list, ignore_index=True)

# Create a DataFrame from the list of valid card data
card_df = pd.DataFrame(valid_card_data_df)

# Save the DataFrame to a Parquet file for better performance and storage efficiency
parquet_path = current_dir / 'card_schema.parquet'
card_df.to_parquet(parquet_path, index=False)
