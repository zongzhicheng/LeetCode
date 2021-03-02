"""
No.304：二维区域和检索 - 矩阵不可变
难度：中等

问题描述：

    给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
    子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例：

    给定 matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]

    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12
     
提示：

    你可以假设矩阵不可变。
    会多次调用 sumRegion 方法。
    你可以假设 row1 ≤ row2 且 col1 ≤ col2 。

解题思路：

    和No.303：区域和检索 - 数组不可变类似
    先求出preSum，定义 preSum[i][j] 表示 从 [0,0] 位置到 [i,j] 位置的子矩形所有元素之和。
    如果求 preSum[i][j] 表示的话，对应了以下的递推公式：
        preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + matrix[i][j]
    再根据preSum求子矩阵所有元素之和，
    如果要求 [row1, col1] 到 [row2,col2] 的子矩形的面积的话，用 preSum 对应了以下的递推公式：
        preSum[row2][col2] - preSum[row2][col1 - 1] - preSum[row1 - 1][col2] + preSum[row1 - 1][col1 - 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable

"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            M, N = 0, 0
        else:
            M, N = len(matrix), len(matrix[0])
        self.preSum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                self.preSum[i + 1][j + 1] = self.preSum[i][j + 1] + self.preSum[i + 1][j] - self.preSum[i][j] + \
                                            matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row2 + 1][col1] - \
               self.preSum[row1][col2 + 1] + self.preSum[row1][col1]


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    result = obj.sumRegion(2, 1, 4, 3)
    print(result)
