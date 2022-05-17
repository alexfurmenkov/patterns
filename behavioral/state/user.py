from typing import List


class User:
    """
    The class represents a User.
    """

    def __init__(self, username: str, age: int, posts: List[str], friends: List[str]):
        self.username = username
        self.age = age
        self.posts = posts
        self.friends = friends
