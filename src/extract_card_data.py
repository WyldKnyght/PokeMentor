import json

# Load local JSON file
def load_card_data():
    json_file_path = r"M:\DEV_Projects\PokeMentor\data\pokemon-tcg-data\cards\en\"
    
    with open(json_file_path, 'r') as file:
        cards_data = json.load(file)
    
    print(f"Total cards: {len(cards_data)}")  # Print total number of cards loaded
    return cards_data


def set_to_dict(card_set):
    set_data = {
        "id": card_set.id,
        "name": card_set.name,
        "series": card_set.series,
        "printedTotal": card_set.printedTotal,
        "total": card_set.total,
        "ptcgoCode": card_set.ptcgoCode,
        "releaseDate": card_set.releaseDate,
        "updatedAt": card_set.updatedAt,
        "images": set_image_to_dict(card_set.images) if hasattr(card_set, "images") else {},
    }
    return set_data


def set_image_to_dict(set_image):
    return {
        "symbol": set_image.symbol,
        "logo": set_image.logo
    }


def card_image_to_dict(card_image):
    return {
        "small": card_image.small,
        "large": card_image.large
    }


def ancient_trait_to_dict(ancient_trait):
    if ancient_trait is None:
        return {}
    return {
        "name": ancient_trait.name,
        "text": ancient_trait.text
    }


def ability_to_dict(ability):
    return {
        "name": ability.name,
        "text": ability.text,
        "type": ability.type
    }


def attack_to_dict(attack):
    return {
        "cost": attack.cost if hasattr(attack, "cost") else [],
        "name": attack.name if hasattr(attack, "name") else None,
        "text": attack.text if hasattr(attack, "text") else None,
        "damage": attack.damage if hasattr(attack, "damage") else None,
        "convertedEnergyCost": attack.convertedEnergyCost if hasattr(attack, "convertedEnergyCost") else None
    }


def weakness_to_dict(weakness):
    return {
        "type": weakness.type,
        "value": weakness.value
    }


def legality_to_dict(legality):
    return {
        "standard": list(legality.standard),
        "expanded": list(legality.expanded),
        "unlimited": list(legality.unlimited)
    }


def resistance_to_dict(resistance):
    return {
        "type": resistance.type,
        "value": resistance.value
    }


def card_to_dict(card):
    card_data = {
        "id": card.id,
        "name": card.name,
        "supertype": card.supertype,
        "subtypes": card.subtypes if hasattr(card, "subtypes") else [],
        "level": card.level if hasattr(card, "level") else None,
        "hp": card.hp if hasattr(card, "hp") else None,
        "types": card.types if hasattr(card, "types") else [],
        "evolvesFrom": card.evolvesFrom if hasattr(card, "evolvesFrom") else None,
        "evolvesTo": card.evolvesTo if hasattr(card, "evolvesTo") else [],
        "rules": card.rules if hasattr(card, "rules") else [],
        "ancientTrait": ancient_trait_to_dict(card.ancientTrait) if card.ancientTrait is not None else {},
        "abilities": [ability_to_dict(ability) for ability in card.abilities] if card.abilities is not None else [],
        "attacks": [attack_to_dict(attack) for attack in card.attacks] if card.attacks is not None else [],
        "weaknesses": [weakness_to_dict(weakness) for weakness in
                       card.weaknesses] if card.weaknesses is not None else [],
        "resistances": [resistance_to_dict(resistance) for resistance in
                        card.resistances] if card.resistances is not None else [],
        "retreatCost": card.retreatCost if hasattr(card, "retreatCost") else [],
        "convertedRetreatCost": card.convertedRetreatCost if hasattr(card, "convertedRetreatCost") else None,
        "set": set_to_dict(card.set) if hasattr(card, "set") else {},
        "number": card.number if hasattr(card, "number") else None,
        "artist": card.artist if hasattr(card, "artist") else None,
        "rarity": card.rarity if hasattr(card, "rarity") else None,
        "flavorText": card.flavorText if hasattr(card, "flavorText") else None,
        "legalities": legality_to_dict(card.legalities) if card.legalities is not None else {},
        "regulationMark": card.regulationMark if hasattr(card, "regulationMark") else None,
        "images": card_image_to_dict(card.images) if hasattr(card, "images") else {}
    }
    return card_data


def save_cards_to_json(cards, file_path):
    # Convert Card objects to dictionaries
    cards_data = [card_to_dict(card) for card in cards]

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(cards_data, file, ensure_ascii=False, indent=4)


def main():
    cards = load_card_data()
    
    # Create schema from the loaded card data
    schema = create_schema(cards)
    
    # Use the schema for further processing or analysis

def create_schema(cards):
    # Your code to create the schema from the cards data
    schema = {}  # Placeholder, replace with your implementation
    
    # Print the number of cards retrieved
    print(f"Number of cards: {len(cards)}") # example of working with local data

    print("Cards data schema created.")


if __name__ == "__main__":
    main()
