class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class HashNode(object):
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
        
class DoubleNode(object):
    def __init__(self,value,next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous
        
class PriorityNode(object):
    def __init__(self, value, priority, next=None):
        self.value = value
        self.priority=priority
        self.next = next

class LLStack(object):
    def __init__(self):
        self.top = None
                
    def is_empty(self):
        if(self.top is None):
            return True
        else:
            return False
        
    def push(self, e):
        if self.is_empty:
            newElement = Node(e)
            self.top = newElement
            self.top.next = None

        else:
            newElement = Node(e)
            previous=top
            self.top = newElement
            self.top.next=previous
        
        return(self.top)
            
    def pop(self):
        if self.is_empty:
            return None
        else:
            value = self.top.value
            self.top = self.top.next
            return value

class DoubleLinkList(object):
    def __init__(self):
        self.start = None
        self.end = None 

    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False

    def insertNode(self, node):
        if self.is_empty:
            self.start = node
            self.end = self.start
        else:
            self.end.next = node
            newNode.previous = self.end
            self.end = node
        
    def insert(self, pair):
        if self.is_empty:
            newNode = DoubleNode(pair)
            self.start=newNode
            self.end = self.start
        else:
            newNode = DoubleNode(pair)
            self.end.next = newNode
            newNode.previous = self.end
            self.end = newNode
        return newNode
        
    def head(self):
        if self.is_empty:
            return None
        else:
            return self.start
        
    def delete(self, node):
        if self.is_empty:
            return None
        else:
            ahead = node.next
            prev = node.previous
            ahead.previous = node.previous
            prev.next = node.next

    
class LLQueue(object):
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False
        
    def push(self, e):
        if self.is_empty:
            newNode = Node(e)
            self.start=newNode
        else:
            newNode = Node(e)
            self.start.next=newNode
    
    def pop(self):
        if self.is_empty:
            return None
        else:
            value=self.start.value
            self.start=self.start.next
            return value

class TwoStackQueue(object):
    def __init__(self):
        topEn = None
        topDe = None
        
    def is_empty(self):
        if(topEn.is_empty is None and topDe.is_empty is None):
            return True
        else:
            return False
          
    def push(self, e):
            newElement=Node(e)
            previous=topEn
            top=newElement
            top.next=previous
        
    def pop(self):
        if self.is_empty:
            return None
        if topDe is not None:
            temp=topDe.value
            topDe=topDe.next
            return temp
        if topDe is None:
            while topEn is not None:
                previous=topDe
                topDe=topEn
                topDe.next = previous
                topEn=topEn.next
            return(topDe.pop)

class LLPriorityQueue(object):
    def __init__(self):
        start = None
        
    def is_empty(self):
        if(self.start is None):
            return True
        else:
            return False
        
    def insert(self, priority, e):

        curr=start
        while( curr.priority < priority):
            previous=curr
            curr=curr.next
            
        newelement = PriorityNode(e,priority)
        previous.next=newelement
        newelement.next=curr
              
    def peek(self):
        if self.is_empty:
            return None
        else:
            value=start.value
            return value
    
    def pop_min(self):
        if self.is_empty:
            return None
        else:
            value=start.value
            start=start.next
            return value


