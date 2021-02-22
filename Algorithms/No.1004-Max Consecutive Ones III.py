"""
No.1004：最大连续1的个数 III
难度：中等

问题描述：

    给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
    返回仅包含 1 的最长（连续）子数组的长度。

示例 1：

    输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2

    输出：6

    解释：
        [1,1,1,0,0,☆1,1,1,1,1,☆1]
        ☆数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：

    输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3

    输出：10

    解释：
        [0,0,1,1,☆1,☆1,1,1,☆1,1,1,1,0,0,0,1,1,1,1]
        ☆数字从 0 翻转到 1，最长的子数组长度为 10。
 
提示：

    1 <= A.length <= 20000
    0 <= K <= A.length
    A[i] 为 0 或 1 

解题思路：

    【最多可以把 K 个 0 变成 1，求仅包含 1 的最长子数组的长度】
    转换为【找出一个最长的子数组，该子数组内最多允许有 K 个 0】
    · 使用 left 和 right 两个指针，分别指向滑动窗口的左右边界。
    · right 主动右移：right 指针每次移动一步。当 A[right] 为 0，说明滑动窗口内增加了一个 0；
    · left 被动右移：判断此时窗口内 0 的个数，
      如果超过了 K，则 left 指针被迫右移，直至窗口内的 0 的个数小于等于 K 为止。
    · 滑动窗口长度的最大值就是所求

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones-iii

"""


def longestOnes(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    N = len(A)
    res = 0
    left, right = 0, 0
    zeros = 0
    while right < N:
        if A[right] == 0:
            zeros += 1
        while zeros > K:
            if A[left] == 0:
                zeros -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res


if __name__ == '__main__':
    A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    K = 3
    result = longestOnes(A, K)
    print(result)
