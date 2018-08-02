class Node(object):
    """
    Representation for one item in BST
    """
    def __init__(self, key, data):
        """
        Initialize 4 attributes
        key   -- Value int makes Node object comparable
        data  -- Content stored
        left  -- Left pointer to Node whose key <= self.key
        right -- Right pointer to Node whose key > self.key
        """
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return '(%d %s)' % (self.key, self.data)

class Binarytree():
    def __init__(self):
        """
        Initialize BST

        _root -- root Node of the tree
        """
        self._root = None

    def _newnode(self, key, data):
        """
        Private method to create a new Node object
        """
        return Node(key, data)

    def getroot(self):
        return self._root

    def insert(self, key, data='None'):
        """
        Insert a new Node to the tree

        @param key  -- the key's value of this Node
        @param data -- the data stored in this Node
        """
        if self._root is None:
            self._root = self._newnode(key, data)
            return
        # Start from the root until reach one of the leaf nodes
        # following smaller goes left and bigger goes right fashion
        node = self._root
        direct = 0
        while node:
            parent = node
            if key < node.key:
                direct = 0
                node = node.left
            elif key > node.key:
                direct = 1
                node = node.right
            else:
                node.data = data
                return
        inserted = self._newnode(key, data)
# After done parent holds the refer to one leaf node which will be the parent of new inserted
        if direct == 0:
            #print '%d inserted. parent key %s left' % (key, parent.key)
            parent.left = inserted  
        else: 
            #print '%d inserted. parent key %s right' % (key, parent.key)
            parent.right = inserted

    def lookup(self, key):
        def lookup_rec(key, node):
            if node is None:
                return None
            if node.key == key:
                return node
            if key < node.key:
                return lookup_rec(key, node.left)
            else:
                return lookup_rec(key, node.right)

        if self._root is None:
            return None
        return lookup_rec(key, self._root)

    def maxH(self):
        def recurse(node):
            if node is None:
                return 0
            return 1 + max(recurse(node.left), recurse(node.right))
            
        if self._root is None:
            return 0
        return recurse(self._root)

    def minH(self):
        def recurse(node):
            if node is None:
                return 0
            return 1 + min(recurse(node.left), recurse(node.right))
            
        if self._root is None:
            return 0
        return recurse(self._root)

    def balanced(self):
        return self.maxH() - self.minH() <= 1

    def walk_rec(self):
        """
         inorder traversal: left subtree-root-right subtree
        """
        def walk_rec(node):
            if node.left:
                for v1 in walk_rec(node.left):
                    yield v1

            yield (node.key, node.data)
            if node.right:
                for v2 in walk_rec(node.right):
                    yield v2

        if self._root is None: return
        for each in walk_rec(self._root):
            yield each

    def walk_gen(self):
        if self._root is None: return
        stack = []
        node = self._root
        while stack or node:
            if node: #keep
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield (node.key, node.data)
                node = node.right
    
    def print_node(self):
        def print_rec(node):
            if node.left: print_rec(node.left)
            print (node.key, node.data)
            if node.right: print_rec(node.right)
        print_rec(self._root)

    def compare(self, other):
        """
         return true if other tree is subtree
        """
        def recurse(n1, n2):
            if n2 is None: 
                return True
            elif n1 is None:
                return False
            print n1, n2
            if n1.key != n2.key: return False
            return recurse(n1.left, n2.left) and recurse(n1.right, n2.right)

        subroot = self.lookup(other.getroot().key)
        print "start from %s" % str(subroot)
        if not subroot: 
            print "cannot find the start"
            return False

        return recurse(subroot, other.getroot())

if __name__ == '__main__':
    bintree = Binarytree()
    bintree.insert(8, 'aaa')
    bintree.insert(3, 'bbb')
    bintree.insert(10, 'ccc')
    bintree.insert(1, 'ddd')
    bintree.insert(6, 'eee')
    bintree.insert(6, 'fff')
    bintree.insert(13, 'ggg')
    bintree.insert(14, 'hhh')
    
    #bintree.print_node()
    for each in bintree.walk_rec():
        print each

