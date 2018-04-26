class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree():
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if (self.root != None):
            self._add(val, self.root)
        else: #empty
            self.root = Node(val)

    def _add(self, val, node):
        if (val < node.value):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print str(node.value) + ' '
            self._printTree(node.right)

if __name__ == "__main__":
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.printTree()
