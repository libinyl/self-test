from queue import Queue
from typing import List
from testutil.defs import TreeNode

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def binarytree_lev_order(root: TreeNode, res: List[int]):
    if not root:
        return

    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        res.append(node.val)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
