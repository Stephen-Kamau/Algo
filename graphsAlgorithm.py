

class Graph:
    def __init__(self , node):
        self.node = node
        self.links = []

    def AddLinks(self , node):
        self.links.append(Graph(node))


    def DepthFirstSearch(self , array):
        array.append(self.node)
        #iterate all childrens
        for link in self.links:
            self.DepthFirstSearch(array)
        return array

    def breadthFirstSearch(self ,array):
        queue = []
        while len(queue) > 0:
            currNode = queue.pop(0)
            array.append(currNode.node)
            for link in currNode.links:
                queue.append(link)
        return array
