from typing import Optional, Any


class RedisClient:
    """
    Fake Redis client
    """

    def __init__(self, host: str, port: str, access_key: str):
        self._host = host
        self._port = port
        self._access_key = access_key

    def get_data(self, cache_key: str) -> Optional[Any]:
        pass

    def add_data(self, cache_key: str, data: bytes):
        pass
