from typing import List


# 思考模式:
# 1. 递归
# 2. 终止条件
# 3. pivot
# 4. 比较,增减
# 5. 递归继续

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
