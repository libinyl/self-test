from typing import Callable
from sort import heapSort
from sort import quickSort
from search import binarySearch


def _judge_sort(f_qsort: Callable):
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
            return (False, i)
        continue
    return (True, 0)


def judge_quicksort():
    res = _judge_sort(quickSort.quicksort)
    if not res[0]:
        print_mresult("失败: 快速排序 索引:"+str(res[1]))
        return False
    else:
        print_mresult("成功: 快速排序")
        return True


def judge_heapsort():
    res = _judge_sort(heapSort.heapsort)
    if not res[0]:
        print_mresult("失败: 堆排序 索引:"+str(res[1]))
        return False
    else:
        print_mresult("成功: 堆排序")
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
                print_mresult("失败: 二分查找")
                return False
            except ValueError:
                continue

        if t[0].index(t[1], 0, len(t[0])) != f_binary_search(t[0], t[1], 0, len(t[0])):
            print_mresult("失败: 二分查找")
            return False
    print_mresult("成功: 二分查找")
    return True


def print_mresult(s):
    space = "          "
    print(space+s)


def print_dline(s):
    str_dline = "  =========  "
    print("\n"+str_dline+s+str_dline+"\n")


def test_start():
    print_mresult("\n")
    print_dline("daily test begin")

    test_suite = [judge_quicksort(), judge_heapsort(),
                  judge_search(binarySearch.binary_search)]

    def _test():
        for f in test_suite:
            if not f:
                return False
        return True
    res = _test()
    print_dline("daily test result")
    if res:
        print_mresult("测试全部通过!")
    else:
        print_mresult("训练未通过,请加油.")

    print_dline("daily test end")


test_start()
