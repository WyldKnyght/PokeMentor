# parse_card_text_and_fields.py

import re

# Function to parse card text and extract all fields
def parse_card_text(card_text):
    # Define patterns as a dictionary
    patterns = {
        'id': re.compile(r'^\s*#(\d+)\s*$'),
        'name': re.compile(r'^\s*(.+?)\s*$'),
        'supertype': re.compile(r'^\s*(.+?)\s+([A-Za-z]+)\s*$'),
        'subtypes': re.compile(r'^\s*([A-Za-z]+(?:\s*/\s*[A-Za-z]+)*)\s*$'),
        'hp': re.compile(r'^\s*HP\s+(\d+)\s*$'),
        'evolvesFrom': re.compile(r'^\s*Evolution\s+from\s+(.+?)\s*$'),
        'evolvesTo': re.compile(r'^\s*Evolution\s+to\s+(.+?)\s*$'),
        'rules_list': re.compile(r'^\s*(.+?)\s*$'),
        'ancientTrait': (re.compile(r'^\s*Ancient\s+Trait\s*$'), re.compile(r'^\s*(.+?)\s*$')),
        'abilities': (re.compile(r'^\s*Ability:\s+(.+?)\s*$'), re.compile(r'^\s*(.+?)\s+-\s+(.+?)\s+\((.+?)\)\s*$')),
        'attacks': (re.compile(r'^\s*Attack:\s+(.+?)\s*$'), re.compile(r'^\s*(.+?)\s+-\s+(.+?)\s+\((\d+)\)\s+([^\n]*)$')),
        'weaknesses': (re.compile(r'^\s*Weakness:\s+(.+?)\s*$'), re.compile(r'^\s*([A-Za-z]+)\s+\((\d+)\)\s*$')),
        'resistences': (re.compile(r'^\s*Resistance:\s+(.+?)\s*$'), re.compile(r'^\s*([A-Za-z]+)\s+\((\d+)\)\s*$')),
        'retreatCost': re.compile(r'^\s*Retreat\s+Cost:\s+(.+?)\s*$'),
        'convertedRetreatCost': re.compile(r'^\s*Converted\s+Retreat\s+Cost:\s+(\d+)\s*$'),
        'card_set': (re.compile(r'^\s*Set\s+([\w-]+)\s*$'), re.compile(r'^\s*Name:\s+(.+?)\s*$'), re.compile(r'^\s*Series:\s+(.+?)\s*$'), re.compile(r'^\s*Printed\s+Total:\s+(\d+)\s*$'), re.compile(r'^\s*Total:\s+(\d+)\s*$'), re.compile(r'^\s*Standard\s+Legal:\s+(.+?)\s*$'), re.compile(r'^\s*Expanded\s+Legal:\s+(.+?)\s*$'), re.compile(r'^\s*Unlimited\s+Legal:\s+(.+?)\s*$'), re.compile(r'^\s*PTCGO\s+Code:\s+(.+?)\s*$'), re.compile(r'^\s*Release\s+Date:\s+(.+?)\s*$'), re.compile(r'^\s*Updated\s+At:\s+(.+?)\s*$'), re.compile(r'^\s*Symbol:\s+(.+?)\s*$'), re.compile(r'^\s*Logo:\s+(.+?)\s*$')),
        'number': re.compile(r'^\s*Card\s+Number:\s+(.+?)\s*$'),
        'artist': re.compile(r'^\s*Artist:\s+(.+?)\s*$'),
        'rarity': re.compile(r'^\s*Rarity:\s+(.+?)\s*$'),
        'flavorText': re.compile(r'^\s*"(.+?)"\s*$'),
        'nationalPokedexNumbers': re.compile(r'^\s*National\s+Pokedex\s+Numbers:\s+(.+?)\s*$'),
        'legalities': (re.compile(r'^\s*Unlimited\s+Legal:\s+(.+?)\s*$'), re.compile(r'^\s*Standard\s+Legal:\s+(.+?)\s*$'), re.compile(r'^\s*Expanded\s+Legal:\s+(.+?)\s*$')),
        'regulationMark': re.compile(r'^\s*Regulation\s+Mark:\s+(.+?)\s*$'),
        'images': (re.compile(r'^\s*Image:\s+(.+?)\s*$'), re.compile(r'^\s*Large\s+Image:\s+(.+?)\s*$'))
    }

    # Use list comprehension to extract fields
    parsed_data = {field: [dict(zip(('name', 'text', 'type'), values)) for values in zip(*(re.findall(p, card_text) for p in pattern))] if isinstance(pattern, tuple) else extract_field(pattern, card_text) for field, pattern in patterns.items()}

    # Convert subtypes to a list
    if parsed_data['subtypes']:
        parsed_data['subtypes'] = [subtype.strip() for subtype in parsed_data['subtypes'].split(",")]

    # Extract legalities as a dictionary
    if parsed_data['legalities']:
        parsed_data['legalities'] = dict(zip(('unlimited', 'standard', 'expanded'), parsed_data['legalities']))

    # Extract card set data as a dictionary
    if parsed_data['card_set']:
        card_set_fields = ('set_id', 'set_name', 'set_series', 'set_printedTotal', 'set_total', 'set_ptcgoCode', 'set_releaseDate', 'set_updatedAt')
        card_set_legalities = ('set_standard', 'set_expanded', 'set_unlimited')
        card_set_images = ('set_symbol', 'set_logo')
        card_set_data = dict(zip(card_set_fields, parsed_data['card_set'][:len(card_set_fields)]))
        card_set_data['set_legalities'] = dict(zip(card_set_legalities, parsed_data['card_set'][len(card_set_fields):len(card_set_fields)+len(card_set_legalities)]))
        card_set_data['set_images'] = dict(zip(card_set_images, parsed_data['card_set'][len(card_set_fields)+len(card_set_legalities):]))
        parsed_data['card_set'] = card_set_data

    # Convert converted retreat cost to an integer
    if parsed_data['convertedRetreatCost']:
        parsed_data['convertedRetreatCost'] = int(parsed_data['convertedRetreatCost'])

    # Convert national Pokedex numbers to a list of integers
    if parsed_data['nationalPokedexNumbers']:
        parsed_data['nationalPokedexNumbers'] = [int(number.strip()) for number in parsed_data['nationalPokedexNumbers']]

    return parsed_data

# Helper function to extract a field using a pattern
def extract_field(pattern, text):
    try:
        match = pattern.search(text)
        return match.group(1).strip() if match else None
    except AttributeError:
        return None

# Test the function with the sample card text
sample_card_text = """
# Example card text...
"""

parsed_data = parse_card_text(sample_card_text)

# Print the parsed data
for field, value in parsed_data.items():
    print(f"{field}: {value}")