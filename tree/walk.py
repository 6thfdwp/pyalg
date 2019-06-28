"""
              9
            /   \
           4    10
         /   \    \
        3    6     15
            /        \
           5        20
"""
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

def walk_by_level(root):
    pass

if __name__ == '__main__':
    root = Node(9)
    root.left = Node(4)
    root.right = Node(10)
    root.left.left = Node(3)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.right.right = Node(15)
    root.right.right.right = Node(20)

    print walk_preorder(root)
