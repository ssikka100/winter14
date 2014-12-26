from stackqueue import *

class AbstractCache(object):
    def __init__(self, max_size):
        self.max_size = max_size
    def cache(self, key, value):
        pass
    def get_value(self, key):
        "returns None if key is not in cache"
        pass

class MRUCache(object):
    """
    Evict the most recently accessed or inserted element.
    """
    def __init__(self, max_size):
        self.max_size = max_size
        # stack has no duplicates.
        # |stack| == |store|
        # stack and store have exactly same elements
        # adding element to stack is O(1)
        # removing element from stack... 
        self.store = {}
        self.stack = DoubleLinkList()

    def cache(self, key, value):
        if len(self.store) < self.max_size:
            self.store[key] = self.stack.push(key)
            
        else:
            temp = self.stack.top()
            if self.store.has_key(temp):
                del self.store[temp]
            else:
                delkey, old_value = self.store.popitem()
                
            self.stack.delete(key)    
            self.store[key] = self.stack.push(key)

    def get_value(self, key):
        "returns None if key is not in cache"
        if self.store.has_key(key):
            if self.stack.peek:
                self.stack.delete(key)
                temp = self.stack.push(key)
            return temp.value
        
        else:
            return None
    

Cache = MRUCache
