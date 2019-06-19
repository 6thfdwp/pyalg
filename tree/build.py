import random, array, tempfile, heapq
from collections import deque
from bstree import *

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
    Q = collections.deque( [(0, len(sortedlist)-1)] )
    while Q:
        l, r = Q.popleft()
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

def build_full_tree(arr):
    """
    @param arr (list): [1,5,9,null,2,3,4,8]
    @return root (Node) for BinaryTree
          1[0]
        /       \
      5[1]      9[2]
     /  \       /   \
  None   2[4]   3[5]  4[6]
    """

    def build(node, i):
        if i >= len(arr)-1:
            return

        l, r = i*2+1, i*2+2
        lv = arr[l] if l <= len(arr) - 1 else None
        rv = arr[r] if r <= len(arr) - 1 else None
        ln = Node(lv) if lv is not None else None
        rn = Node(rv) if rv is not None else None

        node.left, node.right = ln, rn

        # if not node.left:
            # build(node.left, i*2+1)
            # build(node.right, lv)
        if node.left:
            build(node.left, l)
        if node.right:
            build(node.right, r)

    if not arr:
        return
    root = Node(arr[0])
    build(root, 0)
    # return root
    return Binarytree(root)

def walk_by_level(root):
    Q = deque([(root, 0, None)])
    while Q:
        node, lvl, parent = Q.popleft()
        if parent:
            # yield node.key, lvl, parent.key
            print 'level %d: %d with parent %d' % (lvl, node.key, parent.key)
        if node.left:
            Q.append((node.left, lvl+1, node))
        if node.right:
            Q.append((node.right, lvl+1, node))


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
    l = [3,5,6,8,9,10,15,16]
    # T = build_bintree(l)
    # T = build_bintree_rec(l)

    T = build_full_tree(l)
    walk_by_level(T._root)
    # for n, lvl, parent in walk_by_level(T._root):
        # print 'level %d: %d with parent %d' (lvl, n, parent)
