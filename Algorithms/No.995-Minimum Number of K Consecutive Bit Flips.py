"""
No.995：K 连续位的最小翻转次数
难度：困难

问题描述：

    在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，
    同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。
    返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。

示例 1：

    输入：A = [0,1,0], K = 1

    输出：2

    解释：先翻转 A[0]，然后翻转 A[2]。

示例 2：

    输入：A = [1,1,0], K = 2

    输出：-1

    解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。

示例 3：

    输入：A = [0,0,0,1,0,1,1,0], K = 3

    输出：3

    解释：
        翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
        翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
        翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
 
提示：

    1 <= A.length <= 30000
    1 <= K <= A.length

解题思路：
    结论1：后面区间的翻转，不会影响前面的元素
    结论2：A[i] 翻转偶数次的结果是 A[i] ，翻转奇数次的结果是 A[i]^1（0 ^ 1 = 1、1 ^ 1 = 0）
    直接从左向右遍历一遍，遇到数字为0，则翻转以该数字为起始的 K 个数字（时间复杂度 O(N*K+N)，超时）
    根据结论2，位置i现在的状态，和它被前面 K-1 个元素翻转的次数（奇偶性）有关
    使用队列模拟滑动窗口，该滑动窗口的含义是前面 K-1 个元素中，以哪些位置起始的子区间进行了翻转。
    该滑动窗口从左向右滑动，如果当前位置 i 需要翻转，则把该位置存储到队列中。
    遍历到新位置 j(j<i+k) 时，队列中元素的个数代表了 i 被前面 K-1 个元素翻转的次数
        1.当 i 位置被翻转了偶数次，如果 A[i] 为0，那么翻转后仍为0，当前元素需要翻转；
        2.当 i 位置被翻转了奇数次，如果 A[i] 为1，那么翻转后是0，当前元素需要翻转。
    综上，如果 len(que)%2 == A[i] 时，当前元素需要翻转
    当 i+K>N 时，说明需要翻转大小为 K 的子区间，但是后面剩余的元素不到 K 个了，所以返回 -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips

"""
import collections


def minKBitFlips(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    N = len(A)
    que = collections.deque()
    res = 0
    for i in range(N):
        if que and i >= que[0] + K:
            que.popleft()
        if len(que) % 2 == A[i]:
            if i + K > N:
                return -1
            que.append(i)
            res += 1
    return res


if __name__ == '__main__':
    A = [0, 0, 0, 1, 0, 1, 1, 0]
    K = 3
    result = minKBitFlips(A, K)
    print(result)
