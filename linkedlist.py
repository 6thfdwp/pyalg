import collections

class Node():
    def __init__(self, value):
        self.value = value
        #self.prev = None
        self.next = None

    def __repr__(self):
        return '%s(%r)' % ('Node', self.value)

class LinkedList(collections.MutableSequence):
    def __init__(self, iterable=None):
        self._len = 0
        self._head = None
        self._tail = None
        if iterable is not None: # will automatically call append
            self += iterable

    def __repr__(self):
        node = self._head
        _list = []
        while node:
            _list.append( str(node) )
            node = node.next
        #_list = [ str(self._getnode(i)) for i in range(len(self)) ]
        return '->'.join(_list)

    def _getnode(self, index):
        if self._head is None: # empty
            return None
        node = self._head
        i = 0
        while i < index:
            node = node.next
            if node is None: # index out of range
                return None
            i += 1
        return node

    """
      Protocol for collections
      Provide index based operations on LinkedList object
    """
    def __len__(self):
        return self._len
    def __getitem__(self, index):
        return self._getnode(index)
    def __setitem__(self, index, value):
        node = self._getnode(index)
        node.value = value
    def __delitem__(self, index):
        node = self._getnode(index)
        if node is None:
            return
        if node == self._head:
            self._head = node.next
        else:
            pre = self._getnode(index-1)
            pre.next = node.next
            if node == self._tail:
                self._tail = pre

    def append(self, value):
        newnode = Node(value)
        if self._head is None:
            self._head = newnode
        else:
            self._tail.next = newnode

        self._tail = newnode
        self._len += 1

    def insert(self, index, value):
        node = self._getnode(index)
        if node is None:
            return
        newnode = Node(value)
        temp = node.next
        node.next = newnode
        newnode.next = temp

        self._len += 1

    def reverse_(self):
        def recurse(self, prev, node):
            if node is None:
                return
            # recursively go to the tail first
            recurse(self, node, node.next)
            if node == self._tail:
                self._head = node
            node.next = prev
            if prev is None:
                self._tail = node

        recurse(self, None, self._head)

    def reverse(self):
        prev, cur = None, self._head 
        self._tail = cur
        while cur:
            # Change the next pointer to refer to its previous node
            temp = cur.next
            cur.next = prev
            # Move prev and cur pointer forward to change next node
            prev = cur
            cur = temp
        self._head = prev

if __name__ == '__main__':
    iterable = [i for i in range(10)]
    ll = LinkedList(iterable)
    print ll
    ll.reverse_()
    print ll

    ll.append('nnnn')
    print ll
    #ll.append(15)
