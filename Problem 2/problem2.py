class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Compression:
    def __init__(self):
        self.value = None
        
    def setData(self, string):
        pass
    
    def doCompression(self):
        pass
    
class Application:
    def __init__(self):
        self.algorithms = []
        self.currentAlgorithm = None
        
    def addCompressionAlgorithm(self, obj):
        self.algorithms.append(obj)
        
    def selectCurrentAlgorithm(self, id):
        for algorithm in self.algorithms:
            if algorithm.id == id:
                currentAlgorithm = algorithm
                
    
    