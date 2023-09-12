# Filename: create_pandas_schema.py

import sys
import os
import pandas as pd
import json
from schema_utils import get_set_schema, get_card_schema, create_empty_card_dataframe
import glob

# Get the project root directory (two levels up from the current script's directory)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the project root directory to the Python path
sys.path.append(project_root)

# Import schema-related functions using absolute import
from schema_utils import load_set_attributes_data

# Adjust the path to the JSON data files using os.path.join()
set_data_path = os.path.join(project_root, 'data', 'pokemon-tcg-data', 'sets', 'en.json')

# Corrected path to the card data folder using os.path.join()
card_data_folder = os.path.join(project_root, 'data', 'pokemon-tcg-data', 'cards', 'en')

# Load set schema and card schema using functions from schema_utils.py
set_schema = get_set_schema(project_root)
card_schema = get_card_schema(project_root)

# Create an empty DataFrame for card data based on the card schema
card_df = create_empty_card_dataframe(card_schema)

# Initialize an empty list to store valid card data
valid_card_data_list = [pd.json_normalize(json.loads(open(f, 'r', encoding='utf-8').read())) for f in glob.glob(os.path.join(card_data_folder, '*.json')) if json.loads(open(f, 'r', encoding='utf-8').read())]

# Concatenate the list of DataFrames into a single DataFrame with a sequential index
valid_card_data_df = pd.concat(valid_card_data_list, ignore_index=True)

# Save the DataFrame to a Parquet file for better performance and storage efficiency
parquet_path = os.path.join(os.path.dirname(__file__), 'card_schema.parquet')
valid_card_data_df.to_parquet(parquet_path, index=False, compression='snappy')