"""
No.338：比特位计数
难度：中等

问题描述：

    给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1：

    输入：2

    输出：[0,1,1]

示例 2：

    输入：5

    输出：[0,1,1,2,1,2]

进阶：

    给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
    要求算法的空间复杂度为O(n)。
    你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

解题思路：

    首先最容易想的做法就是直接遍历统计
    时间复杂度为O(N*sizeof(int))、空间复杂度为O(1)
    其次可以把i分为两个情况：
        · 如果i是偶数，那么它的二进制1的位数与i/2的二进制1的位数相等
        因为偶数的二进制末尾是 0，右移一位等于 i / 2，而二进制中 1 的个数没有变化
        · 如果 i 是奇数，那么它的二进制 1 的位数 = i - 1 的二进制位数 + 1
        因为奇数的二进制末尾是 1，如果把末尾的 1 去掉就等于 i - 1。
        又 i - 1 是偶数，所以奇数 i 的二进制 1 的个数等于 i / 2 中二进制 1 的位数 +1
    所以可以得到状态转移方程：res[i] = res[i >> 1] + (i & 1)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits

"""


def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    # 直接遍历与统计
    # res = []
    # for i in range(num + 1):
    #     res.append(bin(i).count("1"))
    # return res
    res = [0] * (num + 1)
    for i in range(1, num + 1):
        res[i] = res[i >> 1] + (i & 1)
    return res


if __name__ == '__main__':
    num = 5
    result = countBits(num)
    print(result)
