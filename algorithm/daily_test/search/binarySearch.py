from typing import List


def binary_search(arr: List[int], x: int, begin: int, end: int):
    if not arr:
        raise ValueError(str(x) + " is not in the list")

    l = begin
    r = end
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    if r == end:
        raise ValueError(str(x) + " is not in the list")
    return l
