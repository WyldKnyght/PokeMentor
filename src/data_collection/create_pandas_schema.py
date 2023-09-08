import pandas as pd
import json
from utils.schema_utils import get_set_schema, get_card_schema, load_set_attributes_data, create_empty_card_dataframe
from pathlib import Path

# Get the absolute path of the current directory
current_dir = Path(__file__).resolve().parent

# Adjust the path to the JSON data files using pathlib
set_data_path = current_dir.parent / 'data' / 'pokemon-tcg-data' / 'sets' / 'en.json'
card_data_folder = current_dir.parent / 'data' / 'pokemon-tcg-data' / 'cards' / 'en'

# Load set schema and card schema using functions from schema_utils.py
set_schema = get_set_schema()
card_schema = get_card_schema()

# Load the set attributes data from a JSON file
set_attributes_data = load_set_attributes_data(set_data_path)

# Create an empty DataFrame for card data based on the card schema
card_df = create_empty_card_dataframe(card_schema)

# Initialize an empty list to store valid card data
valid_card_data_list = []

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
card_df.to_parquet('card_schema.parquet', index=False)
