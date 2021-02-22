"""
No.766：托普利茨矩阵
难度：简单

问题描述：

    给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true；否则，返回 false 。
    如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

示例 1：

    输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

    输出：true

    解释：
        在上述矩阵中, 其对角线为:
        "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
        各条对角线上的所有元素均相同, 因此答案是 True 。

示例 2：

    输入：matrix = [[1,2],[2,2]]

    输出：false

    解释：对角线 "[1, 2]" 上的元素不同。

提示：

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 20
    0 <= matrix[i][j] <= 99
 
进阶：

    如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
    如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？

解题思路：

    笨方法：遍历每条对角线，判断每条对角线上元素是否都相等
    利用python切片，只要每个元素都跟其右下角元素相等就行了

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/toeplitz-matrix

"""


def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    # 行数 - 1
    for i in range(len(matrix) - 1):
        # 对比每个元素和右下角元素
        if matrix[i][:-1] != matrix[i + 1][1:]:
            return False
    return True


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    result = isToeplitzMatrix(matrix)
    print(result)
