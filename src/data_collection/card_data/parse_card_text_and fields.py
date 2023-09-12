from attribute_patterns import patterns  # Import patterns from attribute_patterns.py


# Function to parse card text and extract all fields
def parse_card_text(card_text):
    # Initialize parsed_data dictionary
    parsed_data = {}

    # Use patterns from attribute_patterns.py to extract fields
    for field, pattern in patterns.items():
        match = pattern.search(card_text)
        if match:
            parsed_data[field] = match.group(1).strip()
        else:
            parsed_data[field] = None

    # Convert subtypes to a list
    if 'subtypes' in parsed_data and parsed_data['subtypes']:
        parsed_data['subtypes'] = [subtype.strip() for subtype in parsed_data['subtypes'].split(",")]

    # Extract legalities as a dictionary
    legalities = {}
    for key in ['unlimited', 'standard', 'expanded']:
        if key in parsed_data and parsed_data[key]:
            legalities[key] = parsed_data.pop(key)
    parsed_data['legalities'] = legalities

    # Extract card set data as a dictionary
    card_set_data = {}
    for key in ['set_id', 'set_name', 'set_series', 'set_printedTotal', 'set_total', 'set_ptcgoCode',
                'set_releaseDate', 'set_updatedAt', 'set_symbol', 'set_logo']:
        if key in parsed_data and parsed_data[key]:
            card_set_data[key] = parsed_data.pop(key)
    card_set_data['set_legalities'] = {}
    for key in ['set_standard', 'set_expanded', 'set_unlimited']:
        if key in parsed_data and parsed_data[key]:
            card_set_data['set_legalities'][key] = parsed_data.pop(key)
    parsed_data['card_set'] = card_set_data

    # Convert converted retreat cost to an integer
    if 'convertedRetreatCost' in parsed_data and parsed_data['convertedRetreatCost']:
        parsed_data['convertedRetreatCost'] = int(parsed_data['convertedRetreatCost'])

    # Convert national Pokedex numbers to a list of integers
    if 'nationalPokedexNumbers' in parsed_data and parsed_data['nationalPokedexNumbers']:
        parsed_data['nationalPokedexNumbers'] = [int(number.strip()) for number in
                                                 parsed_data['nationalPokedexNumbers']]

    return parsed_data


# Test the function with the sample card text
sample_card_text = """
# Example card text...
"""

sample_parsed_data = parse_card_text(sample_card_text)

# Print the parsed data
for data_field, value in sample_parsed_data.items():
    print(f"{data_field}: {value}")
