import pickle
from abc import ABC, abstractmethod
from typing import Optional, Any

from creational.factories.simple_factory.app_config import AppConfig
from creational.factories.simple_factory.redis_client import RedisClient


class CachingServiceInterface(ABC):
    """
    Must be implemented by concrete caching services.
    """

    @abstractmethod
    def get(self, cache_key: str) -> Optional[Any]:
        """
        Gets an object from cache.
        If an object with given key is not found -> None will be returned.
        """

    @abstractmethod
    def add(self, cache_key: str, data: Any):
        """
        Saves given data into cache.
        """


class InMemoryCachingService(CachingServiceInterface):
    """
    Uses in-memory caching.
    """

    def __init__(self):
        self._cache = {}

    def get(self, cache_key: str) -> Optional[Any]:
        return self._cache.get(cache_key)

    def add(self, cache_key: str, data: Any):
        self._cache[cache_key] = data


class RedisCachingService(CachingServiceInterface):
    """
    Uses Redis caching.
    """

    def __init__(self, config: AppConfig):
        self._redis_client = RedisClient(
            host=config["REDIS_HOST"],
            port=config["REDIS_PORT"],
            access_key=config["REDIS_ACCESS_KEY"],
        )

    def get(self, cache_key: str) -> Optional[Any]:
        data = self._redis_client.get_data(cache_key)
        if not data:
            return None
        return pickle.loads(data)

    def add(self, cache_key: str, data: Any):
        cache_data = pickle.dumps(data)
        self._redis_client.add_data(cache_key, cache_data)


class CachingServiceFactory:
    """
    Factory that returns a caching instance
    based on the app config.
    """

    def __init__(self, config: AppConfig):
        self._config = config

    def get_cache_service(self) -> CachingServiceInterface:
        if self._config["CACHE_TYPE"] == "redis":
            return RedisCachingService(self._config)
        else:
            return InMemoryCachingService()


if __name__ == "__main__":
    app_config = AppConfig()
    factory = CachingServiceFactory(app_config)
    caching_service = factory.get_cache_service()
    caching_service.add("key", {"name": "Aleksei"})
