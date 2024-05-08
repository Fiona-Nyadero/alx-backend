#!/usr/bin/python3
'''Module implements FIFO caching'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''FIFOCache is an inherited class from BaseCaching'''

    def __init__(self):
        '''Initialises the class FIFOCache'''
        super().__init__()

    def put(self, key, item):
        '''Assigns item(value) to a key in the dictionary'''
        if key is None or item is None:
            return
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = next(iter(self.cache_data))
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item

    def get(self, key):
        '''Returns the value linked to a key'''
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
