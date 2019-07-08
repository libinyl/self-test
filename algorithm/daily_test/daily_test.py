from typing import Callable
from sort import heapSort
from sort import quickSort
from search import binarySearch

space = "               "


def _judge_sort(f_qsort: Callable) -> bool:
    l1 = []
    l2 = [1]
    l3 = [1, 2, 3]
    l4 = [3, 2, 1]
    l5 = [1, 2, 1]
    l6 = [2, 1, 1]
    l7 = [1, 1, 2]
    l8 = [6, 4, 6, 8, 2, 4, 1, 3, 3, 5, 7, 5, 4, 76, 5]

    l0 = [l1, l2, l3, l4, l5, l6, l7, l8]
    for i, l in enumerate(l0):
        ll = l.copy()
        f_qsort(ll)
        if ll != sorted(l):
            print("失败: 排序测试索引" + str(i) + "")
            return False
        continue
    return True


def judge_quicksort():
    if not _judge_sort(quickSort.quicksort):
        print("失败: 快速排序")
        return False
    else:
        print(space + "成功: 快速排序")
        return True


def judge_heapsort():
    if not _judge_sort(heapSort.heapsort):
        print("失败: 堆排序")
        return False
    else:
        print(space + "成功: 堆排序")
        return True


def judge_search(f_binary_search: Callable) -> bool:
    t1 = ([], 5)
    t2 = ([1], 1)
    t3 = ([1, 2, 3], 3)
    t4 = ([1, 2, 3], 2)

    l = [t1, t2, t3, t4]
    for t in l:
        if t[1] not in t[0]:
            try:
                f_binary_search(t[0], t[1], 0, len(t[0]))
                print("失败: 二分查找")
                return False
            except ValueError:
                continue

        if t[0].index(t[1], 0, len(t[0])) != f_binary_search(t[0], t[1], 0, len(t[0])):
            print("失败: 二分查找")
            return False
    print(space + "成功: 二分查找")
    return True


def test_start():
    str_begin = "\n\n=========  daily test begin  ==============\n\n"
    str_end = "\n\n=========  daily test end  ==============\n\n"

    print(str_begin)
    test_suite = [judge_quicksort(), judge_heapsort(),
                  judge_search(binarySearch.binary_search)]
    for f in test_suite:
        if not f:
            print("训练未通过,请加油.")
            return
    print("测试全部通过!")
    print(str_end)


test_start()
