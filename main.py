from typing import Any
from abc import ABCMeta, abstractmethod
from collections import deque

########################### Interfaces ##################################
class Cache(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key:int) -> int:
        pass

    @abstractmethod
    def put(self, key:int, val:int):
        pass


class CacheAlgorithm(metaclass=ABCMeta):
    @abstractmethod
    def key_used(self, key: int):
        """Update the key access order as per the implemented algorithm"""
    
    @abstractmethod
    def add_key(self, key: int):
        """Update the val for the key as per the implemented algorithm"""
    
    @abstractmethod
    def evict(self):
        """Implement Eviction algorithm"""
    
    @abstractmethod
    def is_cache_full(self) -> bool:
        """Implement algo to check if cache is full"""



#########################################################################
########################### Exceptions ##################################
class CacheKeyNotFoundException(Exception):
    """Cache Key Not Found"""

class CacheFullException(Exception):
    """Cache is Full"""
#########################################################################
class LRUCacheAlgorithm(CacheAlgorithm):
    def __init__(self, capacity: int) -> None:
        self.ds = deque()
        self.MAX = capacity
        self.current_size = 0
    
    def is_cache_full(self) -> bool:
        return self.current_size == self.MAX

    def key_used(self, key: int):
        # Bring the used key to the END OF THE QUEUE (Most Recently Used)
        self.ds.remove(key)
        self.ds.append(key) # MRU
    
    def add_key(self, key: int):
        self.ds.append(key)

    def evict(self):
        return self.ds.popleft()


class DefaultCache(Cache):
    def __init__(self, capacity: int) -> None:
        self.data = dict() # Uses InMemoryCache
        self.algo: CacheAlgorithm = LRUCacheAlgorithm(capacity)
    
    def get(self, key: int) -> int:
        if key in self.data:
            # tell cache_algo that key was accessed.
            self.algo.key_used(key)
            return self.data[key]
        raise CacheKeyNotFoundException
    
    def put(self, key: int, val: int):
        if key in self.data:
            # means key is already present in cache and we need to update it
            self.algo.key_used(key)
            self.data[key] = val
        else:
            # Check if cache is full
            if self.algo.is_cache_full():
                evicted_key = self.algo.evict()
                self.data.pop(evicted_key)
            try:
                self.algo.add_key(key)
                self.data[key] = val
            except CacheFullException:
                print("Something went wrong!")
                raise CacheFullException


class CacheFactory:
    default_cache = DefaultCache
    lru_cache = DefaultCache

if __name__=='__main__':
    X = 5
    cache = CacheFactory.lru_cache(capacity=X)
    
    # Test 1 : Try to get a key if not present
    try:
        cache.get(5)
    except CacheKeyNotFoundException:
        print("Test 1 passed")
    except Exception:
        print("Test 1 Failed")
    
    # Test 2 Normal put and get operation: 
    cache.put(1, 100)
    cache.put(2, 500)
    assert cache.get(1) == 100, "Test 2 Failed"
    assert cache.get(2) == 500, "Test 2 Failed"

    # Test 3 Try to full the cache
    for i in range(20):
        cache.put(i, i*i)
    