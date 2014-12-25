class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class AbstractCache(object):
    def __init__(self, max_size):
        self.max_size = max_size
    def cache(self, key, value):
        pass
    def get_value(self, key):
        "returns None if key is not in cache"
        pass

class MRUCache(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.store = {}
        self.top = None
        
    def cache(self, key, value):
        if len(self.store) < self.max_size:
            self.store[key] = value
        else:
            temp = self.pop()
            del self.store[temp]
            self.store[key] = value
            
    def get_value(self, key):
        "returns None if key is not in cache"
        if self.store.has_key(key):
            self.top = self.push(key)
            return self.store[key]
        else:
            return None

    def is_empty(self):
        if(self.top is None):
            return True
        else:
            return False
        
    def push(self, e):
        if self.is_empty:
            newElement = Node(e)
            top = newElement
            top.next = None
        else:
            newElement = Node(e)
            previous=top
            top = newElement
            top.next=previous        
        return(top)

    def pop(self):
        if self.is_empty:
            return None
        else:
            value=top.value
            top=top.next
            return value

Cache = MRUCache
