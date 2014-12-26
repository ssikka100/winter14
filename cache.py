from stackqueue import *

class AbstractCache(object):
    def __init__(self, max_size):
        self.max_size = max_size
    def cache(self, key, value):
        pass
    def get_value(self, key):
        "returns None if key is not in cache"
        pass

class LRUCache(object):
    """
    Evict the least recently accessed element.
    """
    def __init__(self, max_size):
        self.max_size = max_size 
        self.cacheMem = {}
        self.trackLRU = DoubleLinkList()

    def cache(self, key, value):
        if self.cacheMem.has_key(key):
            mapNode = self.cacheMem[key]
            self.trackLRU.delete(mapNode)
            new = self.trackLRU.insert(value)
            self.cacheMem[key] = new
          
        else:
            if len(self.cacheMem) < self.max_size:
                 new = self.trackLRU.insert(value)
                 self.cacheMem[key] = new
                
            else:
                temp = self.trackLRU.head()
                if self.cacheMem.has_key(temp):
                    self.trackLRU.delete(temp)
                    del self.cacheMem[key]

                    new = self.trackLRU.insert(value)
                    self.cacheMem[key] = new

    def get_value(self, key):
        "returns None if key is not in cache"
        if self.cacheMem.has_key(key):
            mapNode = self.cacheMem[key]
            value = mapNode.value
            self.trackLRU.delete(mapNode)
            temp = self.trackLRU.insert(mapNode)
            return value        
        else:
            return None
    

Cache = LRUCache
