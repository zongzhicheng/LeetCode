"""
No.896：单调数列
难度：简单

问题描述：

    如果数组是单调递增或单调递减的，那么它是单调的。
    如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。
    如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
    当给定的数组 A 是单调数组时返回 true，否则返回 false。

示例 1：

    输入：[1,2,2,3]

    输出：true

示例 2：

    输入：[6,5,4,4]

    输出：true

示例 3：

    输入：[1,3,2]

    输出：false

示例 4：

    输入：[1,2,4,5]

    输出：true

示例 5：

    输入：[1,1,1]

    输出：true

提示：

    1 <= A.length <= 50000
    -100000 <= A[i] <= 100000

解题思路：

    简单题重拳出击，一次遍历

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/monotonic-array

"""


def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    dec, inc = True, True
    N = len(A)
    for i in range(1, N):
        if A[i] > A[i - 1]:
            dec = False
        if A[i] < A[i - 1]:
            inc = False
    if not inc and not dec:
        return False
    return True


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10, 16, 18, 20]
    result = isMonotonic(A)
    print(result)
