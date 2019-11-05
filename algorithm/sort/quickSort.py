from typing import List


# 思路:
# 两大部分:
# 1. 先分治,再递归
# 2. 分治要求新增变量
# 1. cutoff,注意 ij 增减了两次
# 2. 中间交换 1 次
# 3. 先分治,再递归
# 递归的参数: 参数左边界到 j, i 到参数右边界

def _qs(arr: List[int], fst: int, lst: int):

    i, j = fst, lst
    if i >= j:
        return

    pivot = arr[fst]
    while(i <= j):
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    _qs(arr, fst, j)
    _qs(arr, i, lst)


def quicksort(arr: List[int]):
    _qs(arr, 0, len(arr)-1)
    return
