"""
No.832：翻转图像
难度：简单

问题描述：

    给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
    水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
    反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

示例 1：

    输入：[[1,1,0],[1,0,1],[0,0,0]]

    输出：[[1,0,0],[0,1,0],[1,1,1]]

    解释：
        首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
         然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]

示例 2：

    输入：[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

    输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

    解释：
        首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
         然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 
提示：

    1 <= A.length = A[0].length <= 20
    0 <= A[i][j] <= 1

解题思路：

    方法一：先翻转每行，再把0→1，1→0
    方法二：一边左右翻转，一边修改数字

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flipping-an-image

"""


def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    # 时间复杂度O(2 * N  ^2)
    """ 
    rows = len(A)
    cols = len(A[0])
    for row in range(rows):
        # 倒置
        A[row] = A[row][::-1]
        for col in range(cols):
            A[row][col] ^= 1
    return A
    """
    # 时间复杂度O(N^2)
    N = len(A)
    for i in range(N):
        for j in range((N + 1) // 2):
            A[i][j], A[i][N - 1 - j] = 1 - A[i][N - 1 - j], 1 - A[i][j]
    return A


if __name__ == '__main__':
    A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    result = flipAndInvertImage(A)
    print(result)