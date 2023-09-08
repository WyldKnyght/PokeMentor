import sqlite3
import re
import os
import attribute_patterns as patterns

# Function to parse card text and extract all fields
def parse_card_text(card_text):
    parsed_data = {}

    # Extract id
    id_match = re.search(patterns.id_pattern, card_text)
    parsed_data['id'] = id_match.group(1).strip() if id_match else ""

    # Extract name
    name_match = re.search(patterns.name_pattern, card_text)
    parsed_data['name'] = name_match.group(1).strip() if name_match else ""

    # Extract supertype
    supertype_match = re.search(patterns.supertype_pattern, card_text)
    parsed_data['supertype'] = supertype_match.group(1).strip() if supertype_match else ""

    # Extract subtypes
    subtypes_match = re.search(patterns.subtypes_pattern, card_text)
    parsed_data['subtypes'] = [subtype.strip() for subtype in (subtypes_match.group(1).split(","))] if subtypes_match else []

    # Extract hp
    hp_match = re.search(patterns.hp_pattern, card_text)
    parsed_data['hp'] = hp_match.group(1).strip() if hp_match else ""

    # Extract evolvesFrom
    evolves_from_match = re.search(patterns.evolves_from_pattern, card_text)
    parsed_data['evolvesFrom'] = evolves_from_match.group(1).strip() if evolves_from_match else ""

    # Extract evolvesTo
    evolves_to_match = re.search(patterns.evolves_to_pattern, card_text)
    parsed_data['evolvesTo'] = [evolve_to.strip() for evolve_to in (evolves_to_match.group(1).split(","))] if evolves_to_match else []

    # Extract rules_list
    rules_list_match = re.search(patterns.rules_list_pattern, card_text)
    parsed_data['rules_list'] = [rule.strip() for rule in (rules_list_match.group(1).split(","))] if rules_list_match else []

    # Extract ancientTrait
    ancient_trait_name_match = re.search(patterns.ancient_trait_name_pattern, card_text)
    ancient_trait_text_match = re.search(patterns.ancient_trait_text_pattern, card_text)
    if ancient_trait_name_match and ancient_trait_text_match:
        parsed_data['ancientTrait'] = {
            'name': ancient_trait_name_match.group(1).strip(),
            'text': ancient_trait_text_match.group(1).strip()
        }
    else:
        parsed_data['ancientTrait'] = {}

    # Extract abilities
    abilities_name_match = re.findall(patterns.abilities_name_pattern, card_text)
    abilities_text_match = re.findall(patterns.abilities_text_pattern, card_text)
    abilities_type_match = re.findall(patterns.abilities_type_pattern, card_text)
    parsed_data['abilities'] = []
    for i in range(min(len(abilities_name_match), len(abilities_text_match), len(abilities_type_match))):
        ability_data = {
            'name': abilities_name_match[i].strip(),
            'text': abilities_text_match[i].strip(),
            'type': abilities_type_match[i].strip()
        }
        parsed_data['abilities'].append(ability_data)

    # Extract attacks
    attacks_name_match = re.findall(patterns.attacks_name_pattern, card_text)
    attacks_cost_match = re.findall(patterns.attacks_cost_pattern, card_text)
    attacks_converted_energy_cost_match = re.findall(patterns.attacks_converted_energy_cost_pattern, card_text)
    attacks_damage_match = re.findall(patterns.attacks_damage_pattern, card_text)
    attacks_text_match = re.findall(patterns.attacks_text_pattern, card_text)
    parsed_data['attacks'] = []
    for i in range(min(len(attacks_name_match), len(attacks_cost_match), len(attacks_converted_energy_cost_match), len(attacks_damage_match), len(attacks_text_match))):
        attack_data = {
            'name': attacks_name_match[i].strip(),
            'cost': attacks_cost_match[i].strip(),
            'convertedEnergyCost': int(attacks_converted_energy_cost_match[i].strip()),
            'damage': attacks_damage_match[i].strip(),
            'text': attacks_text_match[i].strip()
        }
        parsed_data['attacks'].append(attack_data)

    # Extract weaknesses
    weaknesses_type_match = re.findall(patterns.weaknesses_type_pattern, card_text)
    weaknesses_value_match = re.findall(patterns.weaknesses_value_pattern, card_text)
    parsed_data['weaknesses'] = []
    for i in range(min(len(weaknesses_type_match), len(weaknesses_value_match))):
        weakness_data = {
            'type': weaknesses_type_match[i].strip(),
            'value': weaknesses_value_match[i].strip()
        }
        parsed_data['weaknesses'].append(weakness_data)

    # Extract resistances
    resistences_type_match = re.findall(patterns.resistences_type_pattern, card_text)
    resistences_value_match = re.findall(patterns.resistences_value_pattern, card_text)
    parsed_data['resistences'] = []
    for i in range(min(len(resistences_type_match), len(resistences_value_match))):
        resistence_data = {
            'type': resistences_type_match[i].strip(),
            'value': resistences_value_match[i].strip()
        }
        parsed_data['resistences'].append(resistence_data)

    # Extract retreat cost
    retreat_cost_match = re.search(patterns.retreat_cost_pattern, card_text)
    parsed_data['retreatCost'] = retreat_cost_match.group(1).strip() if retreat_cost_match else ""

    # Extract converted retreat cost
    converted_retreat_cost_match = re.search(patterns.converted_retreat_cost_pattern, card_text)
    parsed_data['convertedRetreatCost'] = int(converted_retreat_cost_match.group(1).strip()) if converted_retreat_cost_match else 0

    # Extract card_set
    card_set_id_match = re.search(patterns.card_set_id_pattern, card_text)
    card_set_name_match = re.search(patterns.card_set_name_pattern, card_text)
    card_set_series_match = re.search(patterns.card_set_series_pattern, card_text)
    card_set_printed_total_match = re.search(patterns.card_set_printed_total_pattern, card_text)
    card_set_total_match = re.search(patterns.card_set_total_pattern, card_text)
    card_set_standard_match = re.search(patterns.card_set_standard_pattern, card_text)
    card_set_expanded_match = re.search(patterns.card_set_expanded_pattern, card_text)
    card_set_unlimited_match = re.search(patterns.card_set_unlimited_pattern, card_text)
    card_set_ptcgo_code_match = re.search(patterns.card_set_ptcgo_code_pattern, card_text)
    card_set_release_date_match = re.search(patterns.card_set_release_date_pattern, card_text)
    card_set_updated_at_match = re.search(patterns.card_set_updated_at_pattern, card_text)
    card_set_symbol_match = re.search(patterns.card_set_symbol_pattern, card_text)
    card_set_logo_match = re.search(patterns.card_set_logo_pattern, card_text)
    parsed_data['card_set'] = {
        'set_id': card_set_id_match.group(1).strip() if card_set_id_match else "",
        'set_name': card_set_name_match.group(1).strip() if card_set_name_match else "",
        'set_series': card_set_series_match.group(1).strip() if card_set_series_match else "",
        'set_printedTotal': int(card_set_printed_total_match.group(1).strip()) if card_set_printed_total_match else 0,
        'set_total': int(card_set_total_match.group(1).strip()) if card_set_total_match else 0,
        'set_legalities': {
            'set_standard': card_set_standard_match.group(1).strip() if card_set_standard_match else "",
            'set_expanded': card_set_expanded_match.group(1).strip() if card_set_expanded_match else "",
            'set_unlimited': card_set_unlimited_match.group(1).strip() if card_set_unlimited_match else ""
        },
        'set_ptcgoCode': card_set_ptcgo_code_match.group(1).strip() if card_set_ptcgo_code_match else "",
        'set_releaseDate': card_set_release_date_match.group(1).strip() if card_set_release_date_match else "",
        'set_updatedAt': card_set_updated_at_match.group(1).strip() if card_set_updated_at_match else "",
        'set_images': {
            'set_symbol': card_set_symbol_match.group(1).strip() if card_set_symbol_match else "",
            'set_logo': card_set_logo_match.group(1).strip() if card_set_logo_match else ""
        }
    }

    # Extract number
    number_match = re.search(patterns.number_pattern, card_text)
    parsed_data['number'] = number_match.group(1).strip() if number_match else ""

    # Extract artist
    artist_match = re.search(patterns.artist_pattern, card_text)
    parsed_data['artist'] = artist_match.group(1).strip() if artist_match else ""

    # Extract rarity
    rarity_match = re.search(patterns.rarity_pattern, card_text)
    parsed_data['rarity'] = rarity_match.group(1).strip() if rarity_match else ""

    # Extract flavor text
    flavor_text_match = re.search(patterns.flavor_text_pattern, card_text)
    parsed_data['flavorText'] = flavor_text_match.group(1).strip() if flavor_text_match else ""

    # Extract national Pokedex numbers
    national_pokedex_numbers_match = re.findall(patterns.national_pokedex_numbers_pattern, card_text)
    parsed_data['nationalPokedexNumbers'] = [number.strip() for number in national_pokedex_numbers_match]

    # Extract legalities
    unlimited_match = re.search(patterns.unlimited_pattern, card_text)
    standard_match = re.search(patterns.standard_pattern, card_text)
    expanded_match = re.search(patterns.expanded_pattern, card_text)
    parsed_data['legalities'] = {
        'unlimited': unlimited_match.group(1).strip() if unlimited_match else "",
        'standard': standard_match.group(1).strip() if standard_match else "",
        'expanded': expanded_match.group(1).strip() if expanded_match else ""
    }

    # Extract regulation mark
    regulation_mark_match = re.search(patterns.regulation_mark_pattern, card_text)
    parsed_data['regulationMark'] = regulation_mark_match.group(1).strip() if regulation_mark_match else ""

    # Extract images
    small_image_match = re.search(patterns.small_image_pattern, card_text)
    large_image_match = re.search(patterns.large_image_pattern, card_text)
    parsed_data['images'] = {
        'small': small_image_match.group(1).strip() if small_image_match else "",
        'large': large_image_match.group(1).strip() if large_image_match else ""
    }

    return parsed_data

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
            resistances TEXT,
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
    db_path = r'\data\parsed_card_data\pokemon_cards.db'

    # Create or connect to the database
    conn = create_database(db_path)

    # Read the card text data (replace with your data source)
    with open(r'\src\card_data.txt', 'r', encoding='utf-8') as file:
        card_data = file.read()

    # Split the card text into individual card entries (assuming each card is separated by a delimiter)
    card_entries = card_data.split('\n\n')

    # Loop through each card entry and parse/store the data
    for card_entry in card_entries:
        parsed_card_data = parse_card_text(card_entry)

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
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            f"Small: {parsed_card_data['images']['small']}, Large: {parsed_card_data['images']['large']}"
        ))
        conn.commit()

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
