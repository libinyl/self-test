from typing import List


def binary_search(arr: List[int], x: int, begin: int, end: int):
    l, r = begin, end
    while (l < r):
        mid = l+int((r-l)/2)
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    if l == end:
        raise ValueError
    return l
