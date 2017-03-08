import random
from string import ascii_lowercase, digits


def generate_code(size: int = 6, chars: str = ascii_lowercase + digits) -> str:
    """Generate a random code."""
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
