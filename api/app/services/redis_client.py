import redis
import os
from typing import Optional


class RedisClient:
    _instance: Optional[redis.Redis] = None

    @classmethod
    def get_client(cls) -> redis.Redis:
        """
        Returns the singleton Redis client instance.
        """
        if cls._instance is None:
            cls._instance = redis.Redis(
                host=os.getenv("REDIS_HOST", "localhost"),
                port=int(os.getenv("REDIS_PORT", 6379)),
                decode_responses=True,
            )
        return cls._instance


# This will ensure the client is initialized when the module is loaded
redis_client = RedisClient.get_client()
