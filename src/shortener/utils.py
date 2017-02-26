import random
from string import ascii_lowercase, digits


def code_generator(size: int = 6, chars: str = ascii_lowercase + digits) -> str:
    """Generates a random short code"""
    return ''.join(random.choice(chars) for _ in range(size))
