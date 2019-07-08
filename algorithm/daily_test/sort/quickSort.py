from typing import List


def _qs(arr: List[int], fst: int, lst: int):
    if fst >= lst:
        return
    privot = arr[fst]
    i, j = fst, lst

    while i <= j:
        while arr[i] < privot: i += 1
        while arr[j] > privot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    _qs(arr, fst, j)
    _qs(arr, i, lst)


def quicksort(arr: List[int]):
    _qs(arr, 0, len(arr) - 1)
    return
