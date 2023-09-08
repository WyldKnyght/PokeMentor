import re
import attribute_patterns as patterns

# Function to parse card text and extract fields
def extract_card_fields(card_text):
    parsed_data = {}

    def extract_field(pattern, group_index=1):
        match = re.search(pattern, card_text)
        return match.group(group_index).strip() if match else ""

    def extract_list_field(pattern, delimiter=','):
        match = re.search(pattern, card_text)
        return [item.strip() for item in match.group(1).split(delimiter)] if match else []

    # Extract fields using helper functions
    parsed_data['id'] = extract_field(patterns.id_pattern)
    parsed_data['name'] = extract_field(patterns.name_pattern)
    parsed_data['supertype'] = extract_field(patterns.supertype_pattern)
    parsed_data['subtypes'] = extract_list_field(patterns.subtypes_pattern)
    parsed_data['hp'] = extract_field(patterns.hp_pattern)
    parsed_data['types'] = extract_list_field(patterns.types_pattern)
    parsed_data['evolvesFrom'] = extract_field(patterns.evolves_from_pattern)
    parsed_data['evolvesTo'] = extract_list_field(patterns.evolves_to_pattern)
    parsed_data['rules_list'] = extract_list_field(patterns.rules_list_pattern)
    
    # Continue extracting other fields...
    parsed_data['ancientTraitName'] = extract_field(patterns.ancient_trait_name_pattern)
    parsed_data['ancientTraitText'] = extract_field(patterns.ancient_trait_text_pattern)

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

    # Continue extracting other fields...

    return parsed_data

# Test the function with the sample card text
parsed_data = extract_card_fields(sample_card_text)

# Print the parsed data
for field, value in parsed_data.items():
    print(f"{field}: {value}")
