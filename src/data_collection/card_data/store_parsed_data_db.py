import sqlite3
import re
import os
from src.data_collection.card_data import attribute_patterns as patterns  # Updated import path

# Function to create or connect to the SQLite database
def create_database(db_path):
    conn = sqlite3.connect(db_path)
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
    return conn

# Main function to parse and store card data in the database
def main():
    # Define the path to the database
    db_path = os.path.join(os.getcwd(), 'data', 'parsed_card_data', 'pokemon_cards.db')

    # Create or connect to the database
    conn = create_database(db_path)

    # Read the card text data (replace with your data source)
    card_data_path = os.path.join(os.getcwd(), 'src', 'card_data.txt')
    with open(card_data_path, 'r', encoding='utf-8') as file:
        card_data = file.read()

    # Split the card text into individual card entries (assuming each card is separated by a delimiter)
    card_entries = card_data.split('\n\n')

    # Loop through each card entry and parse/store the data
    for card_entry in card_entries:
        parsed_card_data = extract_card_fields(card_entry)  # Assuming you have a function named extract_card_fields

        # Store the parsed data in the database
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO pokemon_cards (
                id,
                name,
                supertype,
                subtypes,
                hp,
                types,
                evolvesFrom,
                evolvesTo,
                rulesList,
                ancientTraitName,
                ancientTraitText,
                abilities,
                attacks,
                weaknesses,
                resistences,
                retreatCost,
                convertedRetreatCost,
                cardSet,
                number,
                artist,
                rarity,
                flavorText,
                nationalPokedexNumbers,
                legalities,
                regulationMark,
                images
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            parsed_card_data['id'],
            parsed_card_data['name'],
            parsed_card_data['supertype'],
            ', '.join(parsed_card_data['subtypes']),
            parsed_card_data['hp'],
            ', '.join(parsed_card_data['types']),
            parsed_card_data['evolvesFrom'],
            ', '.join(parsed_card_data['evolvesTo']),
            ', '.join(parsed_card_data['rules_list']),
            parsed_card_data['ancientTrait']['name'],
            parsed_card_data['ancientTrait']['text'],
            ', '.join([f"{ability['name']} ({ability['type']}): {ability['text']}" for ability in parsed_card_data['abilities']]),
            ', '.join([f"{attack['name']} ({attack['cost']}): {attack['damage']} - {attack['text']}" for attack in parsed_card_data['attacks']]),
            ', '.join([f"{weakness['type']} {weakness['value']}" for weakness in parsed_card_data['weaknesses']]),
            ', '.join([f"{resistance['type']} {resistance['value']}" for resistance in parsed_card_data['resistances']]),
            parsed_card_data['retreatCost'],
            parsed_card_data['convertedRetreatCost'],
            parsed_card_data['card_set']['set_name'],
            parsed_card_data['number'],
            parsed_card_data['artist'],
            parsed_card_data['rarity'],
            parsed_card_data['flavorText'],
            ', '.join(parsed_card_data['nationalPokedexNumbers']),
            f"Unlimited: {parsed_card_data['legalities']['unlimited']}, Standard: {parsed_card_data['legalities']['standard']}, Expanded: {parsed_card_data['legalities']['expanded']}",
            parsed_card_data['regulationMark'],
            ', '.join([f"{image['imageUrl']} ({image['imageType']})" for image in parsed_card_data['images']])
        ))
        conn.commit()

    conn.close()

if __name__ == "__main__":
    main()
