class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LLStack(object):
    def __init__(self):
        top = None
                
    def is_empty(self):
        if(top is None):
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


class LLQueue(object):
    def __init__(self):
        start = None
        
    def is_empty(self):
        if start is None:
            return True
        else:
            return False
        
    def push(self, e):
        if self.is_empty:
            newNode = Node(e)
            start=newNode
        else:
            newNode = Node(e)
            start.next=newNode
    
    def pop(self):
        if self.is_empty:
            return None
        else:
            value=start.value
            start=start.next
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
        pass
    def is_empty(self):
        pass
    def insert(self, priority, e):
        pass
    def peek(self):
        pass
    def pop_min(self):
        pass
