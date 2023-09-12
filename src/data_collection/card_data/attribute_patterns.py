# attribute_patterns.py
import re

# Dictionary to store all the regular expressions and their corresponding patterns
patterns = {
    'id': re.compile(r"ID: (.+?)(?=(?:ID:|$))"),
    'name': re.compile(r"Name: (.+?)(?=(?:Name:|$))"),
    'supertype': re.compile(r"Supertype: (.+?)(?=(?:Supertype:|$))"),
    'subtypes': re.compile(r"Subtypes: (.+?)(?=(?:Subtypes:|$))"),
    'hp': re.compile(r"HP: (.+?)(?=(?:HP:|$))"),
    'types': re.compile(r"Types: (.+?)(?=(?:Types:|$))"),
    'evolves_from': re.compile(r"Evolves From: (.+?)(?=(?:Evolves From:|$))"),
    'evolves_to': re.compile(r"Evolves To: (.+?)(?=(?:Evolves To:|$))"),
    'rules_list': re.compile(r"Rules List: (.+?)(?=(?:Rules List:|$))"),
    'ancient_trait_name': re.compile(r"Ancient Trait Name: (.+?)(?=(?:Ancient Trait Name:|$))"),
    'ancient_trait_text': re.compile(r"Ancient Trait Text: (.+?)(?=(?:Ancient Trait Text:|$))"),
    'abilities_name': re.compile(r"Ability Name: (.+?)(?=(?:Ability Name:|$))"),
    'abilities_text': re.compile(r"Ability Text: (.+?)(?=(?:Ability Text:|$))"),
    'abilities_type': re.compile(r"Ability Type: (.+?)(?=(?:Ability Type:|$))"),
    'attacks_name': re.compile(r"Attack Name: (.+?)(?=(?:Attack Name:|$))"),
    'attacks_cost': re.compile(r"Attack Cost: (.+?)(?=(?:Attack Cost:|$))"),
    'attacks_converted_energy_cost': re.compile(r"Attack Converted Energy Cost: (.+?)(?=(?:Attack Converted Energy Cost:|$))"),
    'attacks_damage': re.compile(r"Attack Damage: (.+?)(?=(?:Attack Damage:|$))"),
    'attacks_text': re.compile(r"Attack Text: (.+?)(?=(?:Attack Text:|$))"),
    'weaknesses_type': re.compile(r"Weakness Type: (.+?)(?=(?:Weakness Type:|$))"),
    'weaknesses_value': re.compile(r"Weakness Value: (.+?)(?=(?:Weakness Value:|$))"),
    'resistances_type': re.compile(r"Resistance Type: (.+?)(?=(?:Resistance Type:|$))"),
    'resistances_value': re.compile(r"Resistance Value: (.+?)(?=(?:Resistance Value:|$))"),
    'retreat_cost': re.compile(r"Retreat Cost: (.+?)(?=(?:Retreat Cost:|$))"),
    'converted_retreat_cost': re.compile(r"Converted Retreat Cost: (.+?)(?=(?:Converted Retreat Cost:|$))"),
    'card_set': re.compile(r"Card Set ID: (.+?)(?=(?:Card Set ID:|$))"
                           r"(?:.*?Card Set Name: (.+?)(?=(?:Card Set Name:|$)))?"
                           r"(?:.*?Card Set Series: (.+?)(?=(?:Card Set Series:|$)))?"
                           r"(?:.*?Card Set Printed Total: (.+?)(?=(?:Card Set Printed Total:|$)))?"
                           r"(?:.*?Card Set Total: (.+?)(?=(?:Card Set Total:|$)))?"
                           r"(?:.*?Card Set Standard: (.+?)(?=(?:Card Set Standard:|$)))?"
                           r"(?:.*?Card Set Expanded: (.+?)(?=(?:Card Set Expanded:|$)))?"
                           r"(?:.*?Card Set Unlimited: (.+?)(?=(?:Card Set Unlimited:|$)))?"
                           r"(?:.*?Card Set PTCGO Code: (.+?)(?=(?:Card Set PTCGO Code:|$)))?"
                           r"(?:.*?Card Set Release Date: (.+?)(?=(?:Card Set Release Date:|$)))?"
                           r"(?:.*?Card Set Updated At: (.+?)(?=(?:Card Set Updated At:|$)))?"
                           r"(?:.*?Card Set Symbol: (.+?)(?=(?:Card Set Symbol:|$)))?"
                           r"(?:.*?Card Set Logo: (.+?)(?=(?:Card Set Logo:|$)))?"),
    'number': re.compile(r"Number: (.+?)(?=(?:Number:|$))"),
    'artist': re.compile(r"Artist: (.+?)(?=(?:Artist:|$))"),
    'rarity': re.compile(r"Rarity: (.+?)(?=(?:Rarity:|$))"),
    'flavor_text': re.compile(r"Flavor Text: (.+?)(?=(?:Flavor Text:|$))"),
    'national_pokedex_numbers': re.compile(r"National Pokedex Numbers: (.+?)(?=(?:National Pokedex Numbers:|$))"),
    'unlimited': re.compile(r"Unlimited: (.+?)(?=(?:Unlimited:|$))"),
    'standard': re.compile(r"Standard: (.+?)(?=(?:Standard:|$))"),
    'expanded': re.compile(r"Expanded: (.+?)(?=(?:Expanded:|$))"),
    'regulation_mark': re.compile(r"Regulation Mark: (.+?)(?=(?:Regulation Mark:|$))"),
    'small_image': re.compile(r"Small Image: (.+?)(?=(?:Small Image:|$))"),
    'large_image': re.compile(r"Large Image: (.+?)(?=(?:Large Image:|$))")
}