"""
No.485：最大连续1的个数
难度：简单

问题描述：

    给定一个二进制数组，计算其中最大连续1的个数。

示例：

    输入：[1,1,0,1,1,1]

    输出：3

    解释：开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

注意：

    输入的数组只包含 0 和 1 。
    输入数组的长度是正整数，且不超过 10,000。

解题思路：

    对数组遍历一次，遍历时需要保存遇到的最后一个0的位置index；
    如果遍历到i位置的数字为0，则更新index为当前位置i；
    如果遍历到i位置的数字为1，那么当前区间共有i-index个连续的1；
    记录遍历过程中所有连续的1的长度的最大值

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones

"""


def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    index = -1
    res = 0
    for i, num in enumerate(nums):
        if num == 0:
            index = i
        else:
            res = max(res, i - index)
    return res


if __name__ == '__main__':
    result = findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    print(result)
