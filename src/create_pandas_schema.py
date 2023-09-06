# src/create_pandas_schema.py
import os
import pandas as pd
import json
from utils.schema_utils import get_set_schema, get_card_schema, load_set_attributes_data, create_empty_card_dataframe, extract_valid_card_data

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Adjust the path to the JSON data files to go up one level and then to the data folder
set_data_path = os.path.join(current_dir, '..', 'data', 'pokemon-tcg-data', 'sets', 'en.json')
card_data_folder = os.path.join(current_dir, '..', 'data', 'pokemon-tcg-data', 'cards', 'en')

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
for filename in os.listdir(card_data_folder):
    if filename.endswith('.json'):
        card_attributes_json_path = os.path.join(card_data_folder, filename)

        # Load card attributes data from a JSON file
        with open(card_attributes_json_path, 'r', encoding='utf-8') as card_json_file:
            card_attributes_data = json.load(card_json_file)

        # Check if card_attributes_data is not None
        if card_attributes_data is not None:
            # Extract valid card data using the schema
            valid_card_data_list.extend(extract_valid_card_data(card_schema, set_schema, card_attributes_data))

# Create a DataFrame from the list of valid card data
card_df = pd.DataFrame(valid_card_data_list)

# Save the DataFrame to a CSV file (you can change the format as needed)
card_df.to_csv('card_schema.csv', index=False)
