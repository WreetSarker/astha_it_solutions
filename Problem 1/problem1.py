class Node:
    def __init__(self):
        self.value = None
        self.child = None
        

class ParentNode:
    def __init__(self):
        self.value = None
    def getInnerHTML(self):
        pass
    def getHTML(self):
        pass
    
class ContainerNode:
    def __init__(self):
        self.root = None
        
    def addNode(self, node):
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current is not None:
                current = current.child
            current.child = node
            
    def removeNode(self, node):
        if self.root is None:
            return False
        else:
            current = self.root
            while current.child.value != node.value:
                current = current.child
            if current.child.child is not None:
                current.child = current.child.child
            else:
                current.child = None
                
                
    def getInnerHTML(self):
        res = ""
        current = self.root
        while current is not None:
            res += current.value
            current = current.child
        return res
    def getHTML(self):
        res = ""
        current = self.root
        while current is not None:
            res += current.value
            current = current.child
        return res