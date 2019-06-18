from bstree import *
import random, array, tempfile, heapq

"""
Construct balanced BST with BFS
"""
def build_bintree(sortedlist):
    """
    Simulate BFS, insert level by level, e.g for array with 8 items
    first mid in the 8 items (0-3-7)
    then  mid in the left half (0-1-2)
    then  mid in the right half (4-5-7)
    and then mid in 0-1-2 and keep continue until one item left

    Time: O(NlogN) insert to BST dynamically
    Space: O(N) for processing Q
    """
    T = Binarytree()
    Q = [(0, len(sortedlist)-1)]
    while Q:
        l, r = Q.pop(0)
        mid = (l + r) / 2
        print '%d-%d-%d' % (l, mid, r)
        T.insert(sortedlist[mid]) # insert(root, key)
        if l <= mid-1:
            # when equals, one item left
            Q.append( (l, mid-1) )
        if r >= mid+1:
            Q.append( (mid+1, r) )
    return T

"""
Construct balanced BST with DFS
"""
def build_bintree_rec(sortedlist):
    """
    Instead of inserting dynamically, can rely on recursive call
    to add leaf nodes first, and backtrack to upper level until root
    The call stack will yield different traversing order
                   0,7
                /
            3 (0,2)
              /
           1 (0,0) (2,2)
           /         \
    0 (0,-1)       2 (3,2)

    Time:  O(N)
    Space: O(logN)
    """
    def recurse(sortedlist, l, r):
        if l > r:
            # backtrack to leaf node
            return None
        m = (l + r) / 2
        print '%d-%d-%d' % (l, m, r)
        node = Node(sortedlist[m])

        node.left = recurse(sortedlist, l, m-1)
        node.right = recurse(sortedlist, m+1, r)
        #
        return node

    root = recurse(sortedlist, 0, len(sortedlist)-1)
    return Binarytree(root)

def find_parent(p, k1, k2):
    def cover(node, key):
        if node is None: return False
        if node.key == key: return True
        return cover(node.left, key) or cover(node.right, key)
    # if both on the left, the first common parent should be one in the left subtree
    if cover(p.left, k1) and cover(p.left, k2):
        return find_parent(p.left, k1, k2)
    if cover(p.right, k1) and cover(p.right, k2):
        return find_parent(p.right, k1, k2)
    # if both are in different subtrees, no need go deeper, return current p
    return p


if __name__ == '__main__':
    # l = [3,6,8,10,15,16,7,9]
    l = [3,5,6,8,9, 10,15,16]
    # T = build_bintree(l)
    T = build_bintree_rec(l)

    for n in T.walk_gen():
        print n
