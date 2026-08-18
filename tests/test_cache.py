"""Tests du module core/cache."""

from pathlib import Path
from tempfile import TemporaryDirectory

from core.cache import Cache


def test_cache_hit_miss():
    with TemporaryDirectory() as tmp:
        cache = Cache(Path(tmp))
        assert cache.get("key1") is None
        cache.set("key1", "value1")
        assert cache.get("key1") == "value1"


def test_cache_ttl_expiry():
    with TemporaryDirectory() as tmp:
        cache = Cache(Path(tmp), ttl_days=0)
        cache.set("key1", "value1")
        assert cache.get("key1") is None
