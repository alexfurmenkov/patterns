import os


class AppConfig:
    """
    Application config.
    """

    def __init__(self):
        self._config: dict = {
            "CACHE_TYPE": os.getenv("CACHE_TYPE"),
            "REDIS_HOST": os.getenv("REDIS_HOST"),
            "REDIS_PORT": os.getenv("REDIS_PORT"),
            "REDIS_ACCESS_KEY": os.getenv("REDIS_ACCESS_KEY"),
        }

    def __getitem__(self, item: str):
        return self._config[item]
