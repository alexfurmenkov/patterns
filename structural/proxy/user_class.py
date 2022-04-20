import secrets


ADMIN_ROLE_NAME: str = 'admin'


class User:
    """
    This class represents a user of the "system"
    """

    def __init__(self, username: str):
        self.username = username
        self._password = secrets.token_hex()
        self._role: str = 'manager'

    @property
    def is_admin(self):
        return bool(self._role == ADMIN_ROLE_NAME)
