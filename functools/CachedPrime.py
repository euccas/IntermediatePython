from functools import lru_cache
import math

# LRU cache maxsize is set to 2, and only 2 results will be saved in the cache. 
@lru_cache(2)
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True