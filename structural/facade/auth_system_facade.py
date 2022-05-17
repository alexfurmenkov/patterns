"""
FACADE PATTERN EXAMPLE

There is a complex authentication system which is represented by a class AuthenticationSystem.
It is responsible for handling authentication, authorization, hashing passwords and generating authentication tokens.

We need to give its users a convenient interface with simple methods like signup and login.
So, AuthenticationSystemFacade class implements this facade.
"""


import hashlib
import json
from base64 import b64encode

USERS_DB: list = []


class UserDoesNotExistException(Exception):
    pass


class UserDBModel:
    """
    This class represents a DB user model.
    It provides a CRUD functional for users.
    """

    def __init__(self, username: str, password: str):
        self.username: str = username
        self._password: str = password

    def _to_model_dict(self) -> dict:
        return {"username": self.username, "password": self._password}

    def save_user_to_db(self) -> type("UserDBModel", (), {}):
        print(f"Saving user record to DB. username={self.username}")
        USERS_DB.append(self._to_model_dict())
        return self

    @classmethod
    def get_user(cls, user_params: dict) -> type("UserDBModel", (), {}):
        """
        Gets a user by given from DB.
        :param user_params: params of user record to get.
        :return: UserDBModel object.
        """
        print(f"Getting user from DB. user params={user_params}")
        for user in USERS_DB:
            # find the record with the same key/value pairs
            if set(user_params.items()).issubset(set(user.items())):
                return cls(**user)
        return None


class AuthenticationSystem:
    """
    This class represents an authentication system.
    """

    def __init__(self, username: str, password: str):
        self.username: str = username
        self._password: str = password

    def _generate_hashed_password(self) -> str:
        """
        Generates hashed password.
        :return: str
        """
        return hashlib.md5(self._password.encode("utf-8")).hexdigest()

    def _generate_authentication_token(self) -> str:
        payload: dict = {"username": self.username}
        utf_8_b64_encoded_token: bytes = b64encode(json.dumps(payload).encode("utf-8"))
        str_b64_encoded_token: str = utf_8_b64_encoded_token.decode("utf-8")
        return str_b64_encoded_token

    def create_new_user(self) -> UserDBModel:
        """
        Generates hashed password and saves user to DB.
        :return:
        """
        hashed_password: str = self._generate_hashed_password()
        user_db_model: UserDBModel = UserDBModel(self.username, hashed_password)
        return user_db_model.save_user_to_db()

    def authenticate_user(self) -> bool:
        """
        Authenticates a user - gets DB record with given username and password.
        :return: True if user with such credentials exists, False if not.
        """
        hashed_password: str = self._generate_hashed_password()
        return bool(
            UserDBModel.get_user(
                {"username": self.username, "password": hashed_password}
            )
        )

    def authorize_user(self) -> str:
        """
        Authorizes a user and returns authentication token.
        :return: authentication token.
        """
        if self.authenticate_user():
            return self._generate_authentication_token()
        else:
            raise UserDoesNotExistException("User with such credentials is not found")


class AuthenticationSystemFacade:
    """
    This class is provides a convenient interface for the client of Authentication system.
    """

    def __init__(self, username: str, password: str):
        self._auth_system_instance: AuthenticationSystem = AuthenticationSystem(
            username, password
        )

    def signup(self) -> dict:
        """
        Creates a new user of the application.
        :return: Created user object
        """
        new_user: UserDBModel = self._auth_system_instance.create_new_user()
        return {
            "status": "Success",
            "message": "User has been created successfully",
            "username": new_user.username,
        }

    def login(self) -> dict:
        """
        Logs user in
        :return: Authentication token
        """
        try:
            authentication_token: str = self._auth_system_instance.authorize_user()
        except UserDoesNotExistException as e:
            return {"status": "Error", "message": str(e)}

        return {
            "status": "Success",
            "message": "User has logged in successfully",
            "authentication_token": authentication_token,
        }


if __name__ == "__main__":
    auth_system_facade: AuthenticationSystemFacade = AuthenticationSystemFacade(
        "alexey", "password"
    )

    signup_response: dict = auth_system_facade.signup()
    print("signup_response", signup_response)

    login_response: dict = auth_system_facade.login()
    print("login_response", login_response)
