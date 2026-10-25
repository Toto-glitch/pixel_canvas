class TokenException(Exception):
    """The token is invalid, expired or damaged"""


class UserAlreadyExistsException(Exception):
    """The user is already exists in app"""


class InvalidCredentialsException(Exception):
    """User credentials are invalid"""


class CooldownException(Exception):
    """This user has cooldown"""
