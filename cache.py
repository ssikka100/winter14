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

    def moveToFront(self, mapNode):
        """Moves a node to front of LRU in constant time"""
        self.trackLRU.delete(mapNode)
        self.trackLRU.insertNode(mapNode)

    def evict(self, key):
        if self.cacheMem.has_key(key):
            mapNode = self.cacheMem[key]
            self.trackLRU.delete(mapNode)
            del self.cacheMem[key]

    def cache(self, key, value):
        if self.cacheMem.has_key(key):
            # move node to front and update value
            mapNode = self.cacheMem[key]
            self.moveToFront(mapNode)
            mapNode.value = value
          
        else:
            if len(self.cacheMem) < self.max_size:
                 # create new node and hashtable entry.
                 pair = (key,value)
                 newNode = self.trackLRU.insert(pair)
                 self.cacheMem[key] = newNode
                
            else:
                # evict LRU , and then create new node and hashtable entry.
                temp = self.trackLRU.head()
                if temp is not None:
                    k,v = temp.value
                    self.evict(k)
                    pair = (key,value)
                    new = self.trackLRU.insert(pair)
                    self.cacheMem[key] = new

    def get_value(self, key):
        "returns None if key is not in cache"
        if self.cacheMem.has_key(key):
            mapNode = self.cacheMem[key]
            value = mapNode.value
            self.moveToFront(mapNode)
            return value        
        else:
            return None
"""
1. insert, less than max size
2. insert, max size, evict LRU
3. get key, should update LRU
4. insert should update LRU
"""

Cache = LRUCache
