from typing import List
from testutil.defs import TreeNode
from queue import Queue

# 测试代码:
#
# l = [1, None,2, 3, 4, 5, 6]
# root = arr2binarytree(l)


def arr2binarytree(arr: List[int]):
    if not arr:
        return None
    n = len(arr)
    if not arr[0]:
        return None
    root = TreeNode(arr[0])
    q = Queue()
    q.put(root)
    i = 1
    while not q.empty():
        node = q.get()
        if i < n:
            if arr[i]:
                node.left = TreeNode(arr[i])
                q.put(node.left)
            i += 1
        if i < n:
            if arr[i]:
                node.right = TreeNode(arr[i])
                q.put(node.right)
            i += 1
    return root
