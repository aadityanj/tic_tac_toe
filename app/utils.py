import re


def is_valid_name(name: str) -> bool:
    """
        Validates the Name
        Args:
            name: Name of the Player
        Returns:
            bool: True if valid
    """
    return re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)
