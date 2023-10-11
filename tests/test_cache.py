from juditha.cache import Cache
from juditha.util import names


def test_cache(eu_authorities):
    cache = Cache()
    for proxy in eu_authorities:
        for value in names(proxy):
            cache.set(value)

    assert cache.get("european parliament") == cache.get("European Parliament")
    assert cache.get("foo") is None

    cache.set("-")
    assert cache.get("-") is None
