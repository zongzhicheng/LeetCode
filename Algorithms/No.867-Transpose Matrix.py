"""
No.867：转置矩阵
难度：简单

问题描述：

    给你一个二维整数数组 matrix，返回 matrix 的 转置矩阵。
    矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：

    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]

    输出：[[1,4,7],[2,5,8],[3,6,9]]

示例 2：

    输入：matrix = [[1,2,3],[4,5,6]]

    输出：[[1,4],[2,5],[3,6]]
 
提示：

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 10^5
    -10^9 <= matrix[i][j] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/transpose-matrix

"""


def transpose(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    M, N = len(matrix), len(matrix[0])
    res = [[0] * M for _ in range(N)]
    for i in range(M):
        for j in range(N):
            res[j][i] = matrix[i][j]
    return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = transpose(matrix)
    print(result)
