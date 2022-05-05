class Request:
    """
    The class that represents a request that should be validated.
    """

    def __init__(self, headers: dict, body: dict):
        self.headers = headers
        self.body = body
        self._user = None

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value: dict):
        self._user = value
