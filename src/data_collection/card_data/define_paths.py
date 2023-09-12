# filename: define_paths.py

from pathlib import Path

def get_project_root():
    """Returns the root directory of the project."""
    current_dir = Path(__file__).parent
    project_root = current_dir.parent.parent  # Adjusted to move up two levels
    return project_root

def get_set_data_path():
    """Returns the file path for the set attributes data."""
    project_root = get_project_root()
    set_data_path = project_root / 'data' / 'pokemon-tcg-data' / 'sets' / 'en.json'
    return set_data_path