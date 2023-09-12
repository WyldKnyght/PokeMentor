import re

# Dictionary storing all the regular expressions and their corresponding patterns
patterns = {
    'id': re.compile(r"\"id\": \"(.+?)\""),
    'name': re.compile(r"\"name\": \"(.+?)\""),
    'supertype': re.compile(r"\"supertype\": \"(.+?)\""),
    'subtypes': re.compile(r"\"subtypes\": \[\"(.+?)\"\]"),
    'level': re.compile(r"\"level\": \"(.+?)\""),
    'hp': re.compile(r"\"hp\": \"(.+?)\""),
    'types': re.compile(r"\"types\": \[\"(.+?)\"\]"),
    'evolvesFrom': re.compile(r"\"evolvesFrom\": \"(.+?)\""),
    'evolvesTo': re.compile(r"\"evolvesTo\": \[\"(.+?)\"\]"),
    'rules': re.compile(r"\"rules\": \[\"(.+?)\"\]"),
    'ancientTrait': re.compile(r"\"ancientTrait\": \{\"name\": \"(.+?)\", \"text\": \"(.+?)\"\}"),
    'abilities': re.compile(r"\"abilities\": \[\{\"name\": \"(.+?)\", \"text\": \"(.+?)\", \"type\": \"(.+?)\"\}\]"),
    'attacks': re.compile(r"\"attacks\": \[\{\"cost\": \[\"(.+?)\"\], \"name\": \"(.+?)\", \"text\": \"(.+?)\", \"damage\": \"(.+?)\", \"convertedEnergyCost\": (\d+)\}\]"),
    'weaknesses': re.compile(r"\"weaknesses\": \[\{\"type\": \"(.+?)\", \"value\": \"(.+?)\"\}\]"),
    'resistances': re.compile(r"\"resistances\": \[\{\"type\": \"(.+?)\", \"value\": \"(.+?)\"\}\]"),
    'retreatCost': re.compile(r"\"retreatCost\": \[\"(.+?)\"\]"),
    'convertedRetreatCost': re.compile(r"\"convertedRetreatCost\": (\d+)"),
    'set': re.compile(r"\"set\": \{\"id\": \"(.+?)\", \"name\": \"(.+?)\", \"series\": \"(.+?)\", \"printedTotal\": (\d+), \"total\": (\d+), \"legalities\": \{\"unlimited\": \"(.+?)\", \"standard\": \"(.+?)\", \"expanded\": \"(.+?)\"\}, \"ptype\": \"(.+?)\"\}"),
    'number': re.compile(r"\"number\": \"(.+?)\""),
    'artist': re.compile(r"\"artist\": \"(.+?)\""),
    'rarity': re.compile(r"\"rarity\": \"(.+?)\""),
    'flavorText': re.compile(r"\"flavorText\": \"(.+?)\""),
    'nationalPokedexNumbers': re.compile(r"\"nationalPokedexNumbers\": \[(\d+)\]"),
    'legalities': re.compile(r"\"legalities\": \{\"unlimited\": \"(.+?)\", \"standard\": \"(.+?)\", \"expanded\": \"(.+?)\"\}"),
    'regulationMark': re.compile(r"\"regulationMark\": \"(.+?)\""),
    'images': re.compile(r"\"images\": \{\"small\": \"(.+?)\", \"large\": \"(.+?)\"\}")
}

# Dictionary representing the "set" object
set_patterns = {
    'set_id': re.compile(r"\"id\": \"(.+?)\""),
    'set_name': re.compile(r"\"name\": \"(.+?)\""),
    'set_series': re.compile(r"\"series\": \"(.+?)\""),
    'set_printedTotal': re.compile(r"\"printedTotal\": (\d+)"),
    'set_total': re.compile(r"\"total\": (\d+)"),
    'set_standard': re.compile(r"\"standard\": \"(.+?)\""),  # Inside 'legalities' hash
    'set_expanded': re.compile(r"\"expanded\": \"(.+?)\""),  # Inside 'legalities' hash
    'set_unlimited': re.compile(r"\"unlimited\": \"(.+?)\""),  # Inside 'legalities' hash
    'set_ptcgoCode': re.compile(r"\"ptcgoCode\": \"(.+?)\""),
    'set_releaseDate': re.compile(r"\"releaseDate\": \"(.+?)\""),
    'set_updatedAt': re.compile(r"\"updatedAt\": \"(.+?)\""),
    'set_symbol': re.compile(r"\"symbol\": \"(.+?)\""),  # Inside 'images' hash
    'set_logo': re.compile(r"\"logo\": \"(.+?)\"")  # Inside 'images' hash