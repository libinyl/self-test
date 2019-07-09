from typing import Callable
from sort import heapSort
from sort import quickSort
from search import binarySearch
from testutil.utils import arr2binarytree
from traversal import binarytree_lev_order

# 关于测试框架的思考:
# 重要参数:1. 用例list  2. 测试函数 3. 传入参数  4. 失败信息  5. 失败索引值  6. 成功信息

# class TestArgs:


########### 排序测试 begin ###########

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

########### 排序测试 end ###########


########### 搜索测试 begin ###########

def judge_search(f_binary_search: Callable) -> bool:
    t1 = ([], 5)
    t2 = ([1], 1)
    t3 = ([1, 2, 3], 3)
    t4 = ([1, 2, 3], 2)

    l = [t1, t2, t3, t4]
    for i, t in enumerate(l):
        if t[1] not in t[0]:
            try:
                f_binary_search(t[0], t[1], 0, len(t[0]))
                print_mresult("失败: 二分查找 索引:"+str(i))
                return False
            except ValueError:
                continue

        if t[0].index(t[1], 0, len(t[0])) != f_binary_search(t[0], t[1], 0, len(t[0])):
            print_mresult("失败: 二分查找 索引:"+str(i))
            return False
    print_mresult("成功: 二分查找")
    return True

########### 搜索测试 end ###########

########### 遍历测试 begin ###########


def judge_binarytree_lev_order(f_binarytree_lev_order: Callable) -> bool:
    l1 = []
    l2 = [1]
    l3 = [3, None]
    l4 = [1, 2, 3, None, 4]
    l5 = [1, None, 5, None, 7]
    l6 = [1, 2, 3, 4, 5, 6, 7, 8]
    ls = [l1, l2, l3, l4, l5, l6]
    for i, l in enumerate(ls):
        root = arr2binarytree(l)
        res = []
        f_binarytree_lev_order(root, res)
        if res != [v for v in l if v]:
            print_mresult("失败: 二叉树层序遍历 索引:"+str(i))
            return (False, i)
    print_mresult("成功: 二叉树层序遍历")
    return True


########### 遍历测试 end ###########


########### 测试工具函数 begin ###########


def print_mresult(s):
    space = "          "
    print(space+s)


def print_dline(s):
    str_dline = "  =========  "
    print("\n"+str_dline+s+str_dline+"\n")

########### 测试工具函数 end ###########


def test_start():
    print_mresult("\n")
    print_dline("daily test begin")

    test_suite = [judge_quicksort(), judge_heapsort(),
                  judge_search(binarySearch.binary_search),
                  judge_binarytree_lev_order(binarytree_lev_order.binarytree_lev_order)]

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
