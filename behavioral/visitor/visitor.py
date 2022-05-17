from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from datetime import datetime
import json


class SerializationVisitorInterface(ABC):
    """
    The interface declares methods for serializing
    different types of DB models classes.
    """

    @abstractmethod
    def serialize_user(self, user: DBUserModel) -> str:
        """
        Serializes DBUserModel object.
        """

    @abstractmethod
    def serialize_post(self, post: DBPostModel) -> str:
        """
        Serializes DBPostModel object.
        """


class SerializationVisitor(SerializationVisitorInterface):
    """
    A concrete serializer.
    """

    def serialize_user(self, user: DBUserModel) -> str:
        dict_to_serialize: dict = {
            "id": user.id,
            "created_at": user.created_at,
            "username": user.username,
        }
        return self._serialize_dict(dict_to_serialize)

    def serialize_post(self, post: DBPostModel) -> str:
        dict_to_serialize: dict = {
            "id": post.id,
            "created_at": post.created_at,
            "description": post.description,
        }
        return self._serialize_dict(dict_to_serialize)

    def _serialize_dict(self, dict_to_serialize: dict) -> str:
        return json.dumps(dict_to_serialize)


class AcceptVisitorInterface(ABC):
    """
    The interface must be implemented by all
    objects that support a serializer visitor.
    """

    @abstractmethod
    def accept_visitor(self, visitor: SerializationVisitorInterface) -> str:
        """
        Must call the corresponding method in the given visitor (double dispatch).
        """


class BaseDBModel(AcceptVisitorInterface, ABC):
    """
    Implements a common behavior for all concrete DB models.
    """

    def __init__(self, record_params: dict):
        self.id: str = record_params["id"]
        self.created_at: str = record_params["created_at"]


class DBUserModel(BaseDBModel):
    """
    Represents a record in "Users" table.
    """

    def __init__(self, record_params: dict):
        super(DBUserModel, self).__init__(record_params)
        self.username: str = record_params["username"]

    def accept_visitor(self, visitor: SerializationVisitorInterface) -> str:
        return visitor.serialize_user(self)


class DBPostModel(BaseDBModel):
    """
    Represents a record in "Posts" table.
    """

    def __init__(self, record_params: dict):
        super(DBPostModel, self).__init__(record_params)
        self.description: str = record_params["description"]

    def accept_visitor(self, visitor: SerializationVisitorInterface) -> str:
        return visitor.serialize_post(self)


if __name__ == "__main__":
    user_obj = DBUserModel(
        {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "username": "John",
        }
    )
    post_obj = DBPostModel(
        {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "description": "Sports Event",
        }
    )

    visitor_obj = SerializationVisitor()
    for model in [user_obj, post_obj]:
        print(model.accept_visitor(visitor_obj))
