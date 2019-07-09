# 思路:
# 1. 二叉树调堆子程序
# 2. 递归的参数: n 有效堆总数,i:当前需要确定的根节点的索引
# 3. 递归退出条件: l r 小于 n
# 4. 三数取大,并交换
# 5. 大根堆调根子程序
# 6. 调根最后参数是 0 原因是


def _heapify(arr, n, i):

    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        _heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        _heapify(arr, n, i)

    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)

    return
