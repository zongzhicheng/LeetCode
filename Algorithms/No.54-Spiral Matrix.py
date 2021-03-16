"""
No.54：螺旋矩阵
难度：中等

问题描述：

    给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：

    matrix = |1 -> 2 -> 3|
             |          ↓|
             |4 -> 5    6|
             |↑         ↓|
             |7 <- 8 <- 9|

    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]

    输出：[1,2,3,6,9,8,7,4,5]

示例 2：

    matrix = |1 -> 2 -> 3 -> 4|
             |               ↓|
             |5 -> 6 -> 7 -> 8|
             |↑              ↓|
             |9 <- 10 <-11<-12|

    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    输出：[1,2,3,4,8,12,11,10,9,5,6,7]

解题思路：

    可以将矩阵看成若干层，首先输出最外层的元素，
    其次输出次外层的元素，直到输出最内层的元素。
    定义矩阵的第 k 层是到最近边界距离为 k 的所有顶点。
    例如，下图矩阵最外层元素都是第 1 层，次外层元素都是第 2 层，剩下的元素都是第 3 层。
        |1 1 1 1 1 1 1|
        |1 2 2 2 2 2 1|
        |1 2 3 3 3 2 1|
        |1 2 2 2 2 2 1|
        |1 1 1 1 1 1 1|
    对于每层，从左上方开始以顺时针的顺序遍历所有元素。
    假设当前层的左上角位于 (top,left)，右下角位于 (bottom,right)，
    按照如下顺序遍历当前层的元素。从左到右遍历上侧元素，依次为 (top,left) 到 (top,right)。
    从上到下遍历右侧元素，依次为 (top+1,right) 到 (bottom,right)。
    如果 left<right 且 top<bottom，则从右到左遍历下侧元素，
    依次为 (bottom,right−1) 到 (bottom,left+1)，
    以及从下到上遍历左侧元素，依次为 (bottom,left) 到 (top+1,left)。
    遍历完当前层的元素之后，将 left 和 top 分别增加 1，
    将 right 和 bottom 分别减少 1，进入下一层继续遍历，直到遍历完所有元素为止。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix

"""


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix or not matrix[0]:
        return list()

    rows, columns = len(matrix), len(matrix[0])
    order = list()
    left, right, top, bottom = 0, columns - 1, 0, rows - 1
    while left <= right and top <= bottom:
        for column in range(left, right + 1):
            order.append(matrix[top][column])
        for row in range(top + 1, bottom + 1):
            order.append(matrix[row][right])
        if left < right and top < bottom:
            for column in range(right - 1, left, -1):
                order.append(matrix[bottom][column])
            for row in range(bottom, top, -1):
                order.append(matrix[row][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return order


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = spiralOrder(matrix)
    print(result)
