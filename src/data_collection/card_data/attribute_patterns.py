# attribute_patterns.py
import re

# Regular expressions to extract various attributes from card text
id_pattern = re.compile(r"ID: (.+?)(?=(?:ID:|$))")
name_pattern = re.compile(r"Name: (.+?)(?=(?:Name:|$))")
supertype_pattern = re.compile(r"Supertype: (.+?)(?=(?:Supertype:|$))")
subtypes_pattern = re.compile(r"Subtypes: (.+?)(?=(?:Subtypes:|$))")
hp_pattern = re.compile(r"HP: (.+?)(?=(?:HP:|$))")
types_pattern = re.compile(r"Types: (.+?)(?=(?:Types:|$))")
evolves_from_pattern = re.compile(r"Evolves From: (.+?)(?=(?:Evolves From:|$))")
evolves_to_pattern = re.compile(r"Evolves To: (.+?)(?=(?:Evolves To:|$))")
rules_list_pattern = re.compile(r"Rules List: (.+?)(?=(?:Rules List:|$))")
ancient_trait_name_pattern = re.compile(r"Ancient Trait Name: (.+?)(?=(?:Ancient Trait Name:|$))")
ancient_trait_text_pattern = re.compile(r"Ancient Trait Text: (.+?)(?=(?:Ancient Trait Text:|$))")
abilities_name_pattern = re.compile(r"Ability Name: (.+?)(?=(?:Ability Name:|$))")
abilities_text_pattern = re.compile(r"Ability Text: (.+?)(?=(?:Ability Text:|$))")
abilities_type_pattern = re.compile(r"Ability Type: (.+?)(?=(?:Ability Type:|$))")
attacks_name_pattern = re.compile(r"Attack Name: (.+?)(?=(?:Attack Name:|$))")
attacks_cost_pattern = re.compile(r"Attack Cost: (.+?)(?=(?:Attack Cost:|$))")
attacks_converted_energy_cost_pattern = re.compile(r"Attack Converted Energy Cost: (.+?)(?=(?:Attack Converted Energy Cost:|$))")
attacks_damage_pattern = re.compile(r"Attack Damage: (.+?)(?=(?:Attack Damage:|$))")
attacks_text_pattern = re.compile(r"Attack Text: (.+?)(?=(?:Attack Text:|$))")
weaknesses_type_pattern = re.compile(r"Weakness Type: (.+?)(?=(?:Weakness Type:|$))")
weaknesses_value_pattern = re.compile(r"Weakness Value: (.+?)(?=(?:Weakness Value:|$))")
resistances_type_pattern = re.compile(r"Resistance Type: (.+?)(?=(?:Resistance Type:|$))")
resistances_value_pattern = re.compile(r"Resistance Value: (.+?)(?=(?:Resistance Value:|$))")
retreat_cost_pattern = re.compile(r"Retreat Cost: (.+?)(?=(?:Retreat Cost:|$))")
converted_retreat_cost_pattern = re.compile(r"Converted Retreat Cost: (.+?)(?=(?:Converted Retreat Cost:|$))")
card_set_pattern = re.compile(r"Card Set ID: (.+?)(?=(?:Card Set ID:|$))"
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
                              r"(?:.*?Card Set Logo: (.+?)(?=(?:Card Set Logo:|$)))?")
number_pattern = re.compile(r"Number: (.+?)(?=(?:Number:|$))")
artist_pattern = re.compile(r"Artist: (.+?)(?=(?:Artist:|$))")
rarity_pattern = re.compile(r"Rarity: (.+?)(?=(?:Rarity:|$))")
flavor_text_pattern = re.compile(r"Flavor Text: (.+?)(?=(?:Flavor Text:|$))")
national_pokedex_numbers_pattern = re.compile(r"National Pokedex Numbers: (.+?)(?=(?:National Pokedex Numbers:|$))")
unlimited_pattern = re.compile(r"Unlimited: (.+?)(?=(?:Unlimited:|$))")
standard_pattern = re.compile(r"Standard: (.+?)(?=(?:Standard:|$))")
expanded_pattern = re.compile(r"Expanded: (.+?)(?=(?:Expanded:|$))")
regulation_mark_pattern = re.compile(r"Regulation Mark: (.+?)(?=(?:Regulation Mark:|$))")
small_image_pattern = re.compile(r"Small Image: (.+?)(?=(?:Small Image:|$))")
large_image_pattern = re.compile(r"Large Image: (.+?)(?=(?:Large Image:|$))")
