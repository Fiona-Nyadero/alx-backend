#!/usr/bin/python3
'''Module implements a LRU Caching algorithm'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LRUCache is an inherited class from BaseCaching'''
    def __init__(self):
        '''Initialises the class LRUCache'''
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        '''Assigns item(value) to a key in the dictionary'''
        if key is None or item is None:
            return

        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.key_order.pop(0)
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))

                self.cache_data[key] = item
                self.key_order.append(key)

    def get(self, key):
        '''Retrieves the key from the dictionary'''
        if key is None or key not in self.cache_data:
            return None
        else:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data.get(key)
