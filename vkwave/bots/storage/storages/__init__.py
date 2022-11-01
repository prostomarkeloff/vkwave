from .default import Storage
from .redis import RedisStorage
from .ttl import TTLStorage
from .vk import VKStorage

__all__ = ("Storage", "RedisStorage", "TTLStorage", "VKStorage")
