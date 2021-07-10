"""
              9
            /   \
           4    10
         /   \    \
        3    6     15
            /        \
           5        20
"""
from collections import deque
from bstree import *

def walk_preorder(root):
    """
    @return (list): [9, 4, 3, 6, 5, 10, 15, 20]

    middle -> left-sub -> right-sub
                |
     middle -> lleft -> llright
    Start from root, process it first before go left, also push right to stack
    Every node in left branch is processed sequentially, when reach to leaf,
    pop its right if it has otherwise pop its parent right
    """
    node = root
    stack, res  = [], []
    while node or stack:
        if node:
            res.append(node.key)
            if node.right:
                stack.append(node.right)
            node = node.left
        elif stack:
            node = stack.pop()

    return res

def recurse_preorder(root):
    def walk(n, result):
        if not n: return
        
        result.append(n.key)
        walk(n.left, result)
        walk(n.right, result)

    result = []
    walk(root, result)
    return result

def group_by_level(root):
    """
    https://leetcode.com/problems/binary-tree-level-order-traversal/

    :type root: TreeNode
    :rtype: List[List[int]]
     [[9], [4,10], [3,6,15], [5,20]]
    """
    if not root: return []

    Q = deque([(root, 0)])
    cur_level = -1
    result = []
    while Q:
        node, lvl = Q.popleft()
        if (lvl != cur_level):
            cur_level = lvl
            level = [node.key]
            result.append(level)
        else:
            result[-1].append(node.key)

        if node.left: Q.append((node.left, lvl+1))
        if node.right: Q.append((node.right, lvl+1)) 
    
    return result

if __name__ == '__main__':
    root = Node(9)
    root.left = Node(4)
    root.right = Node(10)
    root.left.left = Node(3)
    root.left.left.left = Node(30)
    root.left.left.right = Node(40)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.right.right = Node(15)
    root.right.right.right = Node(20)

    # print walk_preorder(root)
    # print recurse_preorder(root)
    print group_by_level(root)
