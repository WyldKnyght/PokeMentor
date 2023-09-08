import spacy
import re
import src.attribute_patterns as patterns

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

def parse_card_text(card_text):
    doc = nlp(card_text)
    parsed_data = {'id': extract_field(card_text, patterns.id_pattern)}

    parsed_data['name'] = extract_field(card_text, patterns.name_pattern)
    parsed_data['supertype'] = extract_field(card_text, patterns.supertype_pattern)
    parsed_data['subtypes'] = extract_list_field(card_text, patterns.subtypes_pattern)
    parsed_data['hp'] = extract_field(card_text, patterns.hp_pattern)
    parsed_data['types'] = extract_list_field(card_text, patterns.types_pattern)
    parsed_data['evolvesFrom'] = extract_field(card_text, patterns.evolves_from_pattern)
    parsed_data['evolvesTo'] = extract_list_field(card_text, patterns.evolves_to_pattern)
    parsed_data['rules_list'] = extract_list_field(card_text, patterns.rules_list_pattern)

    # Extract ancientTrait
    parsed_data['ancientTrait'] = extract_ancient_trait(card_text)

    # Extract abilities
    parsed_data['abilities'] = extract_ability_data(card_text)

    # Extract attacks
    parsed_data['attacks'] = extract_attack_data(card_text)

    # Extract weaknesses and resistances
    parsed_data['weaknesses'] = extract_weaknesses_resistances(card_text, patterns.weaknesses_type_pattern, patterns.weaknesses_value_pattern)
    parsed_data['resistances'] = extract_weaknesses_resistances(card_text, patterns.resistances_type_pattern, patterns.resistances_value_pattern)

    # Extract retreat cost
    parsed_data['retreatCost'] = extract_field(card_text, patterns.retreat_cost_pattern)
    parsed_data['convertedRetreatCost'] = extract_converted_retreat_cost(card_text)

    # Extract card_set
    parsed_data['card_set'] = extract_card_set_data(card_text)

    # Extract other fields
    parsed_data['number'] = extract_field(card_text, patterns.number_pattern)
    parsed_data['artist'] = extract_field(card_text, patterns.artist_pattern)
    parsed_data['rarity'] = extract_field(card_text, patterns.rarity_pattern)
    parsed_data['flavorText'] = extract_field(card_text, patterns.flavor_text_pattern)
    parsed_data['nationalPokedexNumbers'] = extract_list_field(card_text, patterns.national_pokedex_numbers_pattern)
    parsed_data['legalities'] = extract_legalities(card_text)
    parsed_data['regulationMark'] = extract_field(card_text, patterns.regulation_mark_pattern)
    parsed_data['images'] = extract_images(card_text)

    return parsed_data

def extract_field(card_text, pattern):
    match = re.search(pattern, card_text)
    return match[1].strip() if match else ""

def extract_list_field(card_text, pattern):
    match = re.search(pattern, card_text)
    return [item.strip() for item in match[1].split(",")] if match else []

def extract_ancient_trait(card_text):
    name_match = re.search(patterns.ancient_trait_name_pattern, card_text)
    text_match = re.search(patterns.ancient_trait_text_pattern, card_text)
    if name_match and text_match:
        return {'name': name_match[1].strip(), 'text': text_match[1].strip()}
    return {}

def extract_ability_data(card_text):
    names = re.findall(patterns.abilities_name_pattern, card_text)
    texts = re.findall(patterns.abilities_text_pattern, card_text)
    types = re.findall(patterns.abilities_type_pattern, card_text)
    abilities = []
    for i in range(min(len(names), len(texts), len(types))):
        ability_data = {
            'name': names[i].strip(),
            'text': texts[i].strip(),
            'type': types[i].strip()
        }
        abilities.append(ability_data)
    return abilities

def extract_attack_data(card_text):
    names = re.findall(patterns.attacks_name_pattern, card_text)
    costs = re.findall(patterns.attacks_cost_pattern, card_text)
    converted_costs = re.findall(patterns.attacks_converted_energy_cost_pattern, card_text)
    damages = re.findall(patterns.attacks_damage_pattern, card_text)
    texts = re.findall(patterns.attacks_text_pattern, card_text)
    attacks = []
    for i in range(min(len(names), len(costs), len(converted_costs), len(damages), len(texts))):
        attack_data = {
            'name': names[i].strip(),
            'cost': costs[i].strip(),
            'convertedEnergyCost': int(converted_costs[i].strip()),
            'damage': damages[i].strip(),
            'text': texts[i].strip()
        }
        attacks.append(attack_data)
    return attacks

def extract_weaknesses_resistances(card_text, type_pattern, value_pattern):
    types = re.findall(type_pattern, card_text)
    values = re.findall(value_pattern, card_text)
    weaknesses_resistances = []
    for i in range(min(len(types), len(values))):
        data = {
            'type': types[i].strip(),
            'value': values[i].strip()
        }
        weaknesses_resistances.append(data)
    return weaknesses_resistances

def extract_converted_retreat_cost(card_text):
    match = re.search(patterns.converted_retreat_cost_pattern, card_text)
    return int(match[1].strip()) if match else 0

def extract_card_set_data(card_text):
    set_id = extract_field(card_text, patterns.card_set_id_pattern)
    set_name = extract_field(card_text, patterns.card_set_name_pattern)
    set_series = extract_field(card_text, patterns.card_set_series_pattern)
    set_printed_total = int(extract_field(card_text, patterns.card_set_printed_total_pattern)) if extract_field(card_text, patterns.card_set_printed_total_pattern) else 0
    set_total = int(extract_field(card_text, patterns.card_set_total_pattern)) if extract_field(card_text, patterns.card_set_total_pattern) else 0
    set_standard = extract_field(card_text, patterns.card_set_standard_pattern)
    set_expanded = extract_field(card_text, patterns.card_set_expanded_pattern)
    set_unlimited = extract_field(card_text, patterns.card_set_unlimited_pattern)
    set_ptcgo_code = extract_field(card_text, patterns.card_set_ptcgo_code_pattern)
    set_release_date = extract_field(card_text, patterns.card_set_release_date_pattern)
    set_updated_at = extract_field(card_text, patterns.card_set_updated_at_pattern)
    set_symbol = extract_field(card_text, patterns.card_set_symbol_pattern)
    set_logo = extract_field(card_text, patterns.card_set_logo_pattern)

    return {
        'set_id': set_id,
        'set_name': set_name,
        'set_series': set_series,
        'set_printedTotal': set_printed_total,
        'set_total': set_total,
        'set_legalities': {
            'set_standard': set_standard,
            'set_expanded': set_expanded,
            'set_unlimited': set_unlimited
        },
        'set_ptcgoCode': set_ptcgo_code,
        'set_releaseDate': set_release_date,
        'set_updatedAt': set_updated_at,
        'set_images': {
            'set_symbol': set_symbol,
            'set_logo': set_logo
        }
    }

def extract_legalities(card_text):
    unlimited = extract_field(card_text, patterns.unlimited_pattern)
    standard = extract_field(card_text, patterns.standard_pattern)
    expanded = extract_field(card_text, patterns.expanded_pattern)
    return {
        'unlimited': unlimited,
        'standard': standard,
        'expanded': expanded
    }

def extract_images(card_text):
    small_image = extract_field(card_text, patterns.small_image_pattern)
    large_image = extract_field(card_text, patterns.large_image_pattern)
    return {
        'small': small_image,
        'large': large_image
    }
