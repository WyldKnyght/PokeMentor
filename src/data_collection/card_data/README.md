# PokeMentor - Pokémon TCG Data Processing

PokeMentor is a Python project for processing Pokémon Trading Card Game (TCG) data, including parsing card text, storing it in a database, and creating a Pandas schema for analysis. This project is designed to assist hobbyists in improving their Pokémon TCG gameplay and understanding card attributes.

## Project Structure

See folder_structure.txt in project folder. 
To update the folder_structure file run the \admin\create_folder_structure.py code.


## Features

- **Data Parsing**: Scripts for parsing Pokémon TCG card data, including extracting card fields using regular expressions.

- **Database Storage**: Store parsed card data in an SQLite database for efficient retrieval and analysis.

- **Pandas Schema**: Create a Pandas DataFrame schema for card data analysis.

- **Web Scraping**: Utilities for web scraping and data processing.

## Pokémon TCG Data Source

The card data used in this project is cloned from the Pokémon TCG Developers repository at [https://github.com/PokemonTCG/pokemon-tcg-data](https://github.com/PokemonTCG/pokemon-tcg-data). 
We want to give credit and express our gratitude to the Pokémon TCG Developers for providing this valuable resource.

## Usage

1. **Set Up Environment**:
   - Make sure you have Python 3.x installed.
   - Install project dependencies by running `pip install -r requirements.txt`.

2. **Data Collection**:
   - Clone Pokémon TCG Developers pokemon-tcg-data repository in the \data\ folder

3. **Database Creation**:
   - Modify the database path in `store_parsed_data_db.py` if needed.
   - Run `store_parsed_data_db.py` to create or update the database with parsed card data.

4. **Pandas Schema**:
   - Run `create_pandas_schema.py` to create a Pandas schema for card data.

5. **Card Data**:
   - Run `parse_card_text_and_fields.py` to parse the card text and field data.

6. **Store Card Data in Database**:
   - Run `store_parsed_data_db.py` to store parsed data in the database.
