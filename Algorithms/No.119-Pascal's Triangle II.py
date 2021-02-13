"""
No.119：杨辉三角 II
难度：简单

问题描述：

    给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
    在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

    输入: 3
    输出: [1,3,3,1]

解题思路：

    可以直接基于组合数公式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii

"""


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    arr = [1] * (rowIndex + 1)
    for i in range(1, len(arr) - 1):
        arr[i] = arr[i - 1] * (rowIndex - i + 1) // i
    return arr


if __name__ == '__main__':
    result = getRow(3)
    print(result)
