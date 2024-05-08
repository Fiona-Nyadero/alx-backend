#!/usr/bin/env python3
'''Module creates a simple cache algorithm'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        '''Initialises the class BasicCache'''
        self.cache_data = {}

    def put(self, key, item):
        '''Assigns item(value) to a key in the dictionary'''
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''Returns the value linked to a key'''
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
