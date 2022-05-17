import pickle
from abc import ABC, abstractmethod

from behavioral.chain_of_responsibility.exceptions import InvalidRequestError
from behavioral.chain_of_responsibility.request import Request


ADMIN_GROUP_NAME: str = "admin"


class HandlerInterface(ABC):
    """
    An interface that must be implemented by all concrete handlers.
    Defines a method for handling the request.
    """

    @abstractmethod
    def validate(self, request: Request):
        """
        Validates a request using its internal parameters.
        """


class BaseHandler(HandlerInterface):
    """
    The basic class from which all concrete handlers
    should be inherited. Defines some common attributes
    for all handlers.
    """

    def __init__(self):
        self._next_handler = None

    def set_next_handler(self, next_handler: HandlerInterface):
        self._next_handler = next_handler

    def validate(self, request: Request):
        if self._next_handler:
            return self._next_handler.validate(request)
        return None


class PayloadHandler(BaseHandler):
    """
    Validates a request payload.
    """

    def validate(self, request: Request):
        if not isinstance(request.body, dict):
            raise InvalidRequestError("Request body is invalid")
        return super(PayloadHandler, self).validate(request)


class AuthorizationHandler(BaseHandler):
    """
    Ensures that "Authorization" header of the request
    is valid.
    """

    def validate(self, request: Request):
        auth_token: bytes = request.headers.get("Authorization")
        if not auth_token:
            raise InvalidRequestError("Authorization token is missing")

        try:
            # a dummy validation, good apps use JWT
            decoded_token: dict = pickle.loads(auth_token)
        except pickle.UnpicklingError as e:
            print(f"Error occurred while validating a token. Error: {str(e)}")
            raise InvalidRequestError("Authorization token is invalid")

        request.user = decoded_token
        return super(AuthorizationHandler, self).validate(request)


class UserGroupHandler(BaseHandler):
    """
    Checks that user's group is admin if a user is authorized.
    """

    def validate(self, request: Request):
        if request.user and request.user["group"] != ADMIN_GROUP_NAME:
            raise InvalidRequestError("User must be an admin to proceed.")
        return super(UserGroupHandler, self).validate(request)


if __name__ == "__main__":
    # client code
    auth_handler = AuthorizationHandler()
    group_handler = UserGroupHandler()
    payload_handler = PayloadHandler()

    auth_handler.set_next_handler(group_handler)
    group_handler.set_next_handler(payload_handler)

    token: bytes = pickle.dumps({"name": "Aleksei", "group": ADMIN_GROUP_NAME})
    request_to_validate = Request(
        headers={"Authorization": token}, body={"name": "Aleksei"}
    )
    auth_handler.validate(request_to_validate)
