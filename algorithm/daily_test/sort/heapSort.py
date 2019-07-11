# 思路:
# 堆排序主要分两个调整函数,
# 一个是子函数,自上而下,三数取大,沿一条路径递归每三个节点为一组调整
# 另一个是驱动函数,
#   先是反向驱动调整子函数把每个分支都调整为最大堆,进而整体称为最大堆
#   然后把不断把大根堆的根节点与数组最后一个元素交换,并减小大根堆范围,最终升序排列.


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
