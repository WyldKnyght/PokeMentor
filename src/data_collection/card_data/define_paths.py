import os
import glob

# Get the project root directory
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..')
)

# Define paths for the data folder
data_folder = os.path.join(project_root, 'data')
parsed_card_data_folder = os.path.join(data_folder, 'parsed_card_data')
pokemon_tcg_data_folder = os.path.join(data_folder, 'pokemon-tcg-data')

# Define paths for the card data
card_data_folder = os.path.join(pokemon_tcg_data_folder, 'cards', 'en')

# Define paths for the set data
set_data_folder = os.path.join(pokemon_tcg_data_folder, 'sets')
en_set_data_file = os.path.join(set_data_folder, 'en.json')

# Define path for the database
database_path = os.path.join(parsed_card_data_folder, 'pokemon_cards.db')

# Define path for Parquet file
parquet_path = os.path.join(project_root, 'path_to_parquet_directory', 'card_schema.parquet')

# Define json_files
json_files = glob.glob(os.path.join(card_data_folder, '*.json'))

# Export the paths as variables
__all__ = [
    'project_root',
    'data_folder',
    'parsed_card_data_folder',
    'pokemon_tcg_data_folder',
    'card_data_folder',
    'set_data_folder',
    'en_set_data_file',
    'database_path',
    'parquet_path',
    'json_files',  # Include json_files here
]


# Define a get_path function
def get_path(filename):
    """Get the full path to a file or directory within the project."""
    return os.path.join(project_root, filename)
