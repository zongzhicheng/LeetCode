"""
No.73：矩阵置零
难度：中等

问题描述：

    给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
    进阶：

        一个直观的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。
        一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
        你能想出一个仅使用常量空间的解决方案吗？

示例 1：

    输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]

    输出：[[1,0,1],[0,0,0],[1,0,1]]

示例 2：

    输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

提示：

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

解题思路：

    遍历一次矩阵，记录一下每行、列是否出现了 0；如果出现了 0，最终将此行列置为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes

"""


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    if not matrix or not matrix[0]:
        return
    M, N = len(matrix), len(matrix[0])
    row, col = set(), set()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in range(M):
        for j in range(N):
            if i in row or j in col:
                matrix[i][j] = 0
    return matrix


if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    result = setZeroes(matrix)
    print(result)
