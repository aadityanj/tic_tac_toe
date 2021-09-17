import re

def is_valid_name(name:str) -> bool:
    return re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)