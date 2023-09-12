# store_parsed_data_db.py

import sqlite3
from attribute_patterns import patterns
from define_paths import database_path  # Import the database_path variable

# Function to create or connect to the SQLite database
def create_database(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        # Create a table for storing parsed card data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pokemon_cards (
                id TEXT PRIMARY KEY,
                name TEXT,
                supertype TEXT,
                subtypes TEXT,
                hp TEXT,
                types TEXT,
                evolvesFrom TEXT,
                evolvesTo TEXT,
                rulesList TEXT,
                ancientTraitName TEXT,
                ancientTraitText TEXT,
                abilities TEXT,
                attacks TEXT,
                weaknesses TEXT,
                resistences TEXT,
                retreatCost TEXT,
                convertedRetreatCost INTEGER,
                cardSet TEXT,
                number TEXT,
                artist TEXT,
                rarity TEXT,
                flavorText TEXT,
                nationalPokedexNumbers TEXT,
                legalities TEXT,
                regulationMark TEXT,
                images TEXT
            )
        ''')
        conn.commit()

# Main function to parse and store card data in the database
def main():
    # Create or connect to the database
    create_database(database_path)

    # Load JSON data into a Pandas DataFrame
    valid_card_data_df = load_json_files_to_dataframe(card_data_folder)

    if not valid_card_data_df.empty:
        # Convert the DataFrame to a list of dictionaries
        card_data_list = valid_card_data_df.to_dict(orient='records')

        # Store the parsed data in the database
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            for card_data in card_data_list:
                cursor.execute('''
                    INSERT OR REPLACE INTO pokemon_cards (
                        id, name, supertype, subtypes, hp, types, evolvesFrom, evolvesTo,
                        rulesList, ancientTraitName, ancientTraitText, abilities, attacks,
                        weaknesses, resistences, retreatCost, convertedRetreatCost, cardSet,
                        number, artist, rarity, flavorText, nationalPokedexNumbers, legalities,
                        regulationMark, images
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', tuple(card_data.values()))
            conn.commit()
    else:
        print("No valid card data found in JSON files.")

if __name__ == "__main__":
    main()
