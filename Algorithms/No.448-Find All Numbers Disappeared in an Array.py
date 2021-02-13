"""
No.448：找到所有数组中消失的数字
难度：简单

问题描述：

    给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 )的整型数组，
    数组中的元素一些出现了两次，另一些只出现一次。
    找到所有在 [1, n] 范围之间没有出现在数组中的数字。

示例:

    输入:
    [4,3,2,7,8,2,3,1]

    输出:
    [5,6]

解题思路：

    遍历寻找 1~n 是否在数组中存在
    可以使用 set 数据结构，它的查找时间复杂度可以降低到 O(1)。
    时间复杂度：O(N)
    空间复杂度：O(N)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array

"""


def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    counter = set(nums)
    N = len(nums)
    res = []
    for i in range(1, N + 1):
        if i not in counter:
            res.append(i)
    return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))
