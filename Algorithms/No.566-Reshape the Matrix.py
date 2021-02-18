"""
No.566：重塑矩阵
难度：简单

问题描述：

    在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
    给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
    重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
    如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1：

    输入：
        nums =
            [[1,2],
             [3,4]]
        r = 1, c = 4

    输出：[[1,2,3,4]]

    解释：行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。

示例 2：

    输入：
        nums =
            [[1,2],
             [3,4]]
        r = 2, c = 4

    输出：
        [[1,2],
         [3,4]]

    解释：
    没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。

注意：

    给定矩阵的宽和高范围在 [1, 100]。
    给定的 r 和 c 都是正数。

解题思路：

    如果题目给出的矩阵元素个数不等于 r * c，那么无法转换，返回原数组；
    新建一个 r 行、c 列的新数组；
    按行遍历原数组的每个位置，并用 row 和 col 保存应在新数组中填充的当前位置，把原数组的元素放到新数组中的对应位置中。
    row 和 col 的变更规则是：
        每次遍历到一个新位置，则 col += 1；
        如果 col == c，说明到了新数组的列的右边界，需要换行，
        所以 row += 1, col == 0。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reshape-the-matrix

"""


def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    M, N = len(nums), len(nums[0])
    if M * N != r * c:
        return nums
    res = [[0] * c for _ in range(r)]
    row, col = 0, 0
    for i in range(M):
        for j in range(N):
            if col == c:
                row += 1
                col = 0
            res[row][col] = nums[i][j]
            col += 1
    return res
    # 也可以直接使用numpy的reshape()
    # import numpy as np
    # return np.asarray(nums).reshape((r, c))


if __name__ == '__main__':
    nums = [[1, 2], [3, 4]]
    r = 1
    c = 4
    result = matrixReshape(nums, r, c)
    print(nums)
    print(result)
