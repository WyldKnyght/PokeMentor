# main.py
from parser.card_parser import parse_card_text

# Example card text
card_text = """
ID: 123
Name: Pikachu
Types: Electric
HP: 60
Rules List: Quick Attack, Thunderbolt
# ... (other card data)
"""

# Parse the card text
parsed_data = parse_card_text(card_text)

# Access parsed data fields as needed
print(parsed_data)
