"""
No.59：螺旋矩阵 II
难度：中等

问题描述：

    给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
    matrix = |1 -> 2 -> 3|
             |          ↓|
             |8 -> 9    4|
             |↑         ↓|
             |7 <- 6 <- 5|

示例 1：

    输入：n = 3

    输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：

    输入：n = 1

    输出：[[1]]

提示：

    1 <= n <= 20

解题思路：

    思路和 No.54 一样，按层模拟
    定义矩阵的第 k 层是到最近边界距离为 k 的所有顶点。
    例如，下图矩阵最外层元素都是第 1 层，次外层元素都是第 2 层，最内层元素都是第 3 层。
        |1 1 1 1 1 1|
        |1 2 2 2 2 1|
        |1 2 3 3 2 1|
        |1 2 3 3 2 1|
        |1 2 2 2 2 1|
        |1 1 1 1 1 1|
    对于每层，从左上方开始以顺时针的顺序填入所有元素。
    假设当前层的左上角位于 (top,left)，右下角位于 (bottom,right)，按照如下顺序填入当前层的元素。
    从左到右填入上侧元素，依次为 (top,left) 到 (top,right)。
    从上到下填入右侧元素，依次为 (top+1,right) 到 (bottom,right)。
    如果 left<right 且 top<bottom，则从右到左填入下侧元素，依次为 (bottom,right−1) 到 (bottom,left+1)，
    以及从下到上填入左侧元素，依次为 (bottom,left) 到 (top+1,left)。
    填完当前层的元素之后，将 left 和 top 分别增加 1，
    将 right 和 bottom 分别减少 1，进入下一层继续填入元素，直到填完所有元素为止。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii

"""


def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1

    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        for row in range(top + 1, bottom + 1):
            matrix[row][right] = num
            num += 1
        if left < right and top < bottom:
            for col in range(right - 1, left, -1):
                matrix[bottom][col] = num
                num += 1
            for row in range(bottom, top, -1):
                matrix[row][left] = num
                num += 1
        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return matrix


if __name__ == '__main__':
    n = 5
    result = generateMatrix(n)
    print(result)
