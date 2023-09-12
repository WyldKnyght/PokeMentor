import glob
import json
import pandas as pd
from define_paths import card_data_folder, parquet_path, project_root
from schema_utils import get_card_schema, create_empty_card_dataframe


def load_json_files_to_dataframe():
    """
    Load JSON files from a folder into a Pandas DataFrame.

    Returns:
        pd.DataFrame: Combined DataFrame from JSON files.
    """
    json_files = glob.glob(f"{card_data_folder}/*.json")
    dataframes = []

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            dataframes.append(pd.json_normalize(data))

    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    else:
        return pd.DataFrame()


def main():
    # Create an empty DataFrame for card data based on the card schema
    card_schema = get_card_schema(project_root)
    create_empty_card_dataframe(card_schema)  # Removed unused card_df variable

    # Load JSON data into a Pandas DataFrame
    valid_card_data_df = load_json_files_to_dataframe()

    if not valid_card_data_df.empty:
        # Save the DataFrame to a Parquet file for better performance and storage efficiency
        valid_card_data_df.to_parquet(parquet_path, index=False, compression='snappy')
    else:
        print("No valid card data found in JSON files.")


if __name__ == "__main__":
    main()
