"""
No.132：分割回文串 II
难度：困难

问题描述：
    给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
    返回符合要求的 最少分割次数 。

示例 1：

    输入：s = "aab"

    输出：1

    解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

示例 2：

    输入：s = "a"

    输出：0

示例 3：

    输入：s = "ab"

    输出：1

提示：

    1 <= s.length <= 2000
    s 仅由小写英文字母组成

解题思路：

    一、从最长递增子序列谈起
        这个题与「300. 最长递增子序列」非常类似（必须掌握最长递增子序列问题）。
        在最长递增子序列问题中，我们使用了动态规划，定义 dp[i] 表示以 i 结尾的最长递增子序列的长度。
        对每个i的位置，遍历 [0, i)，对判断是否是 nums[i] 是否大于 dp[j] 的，
        如果是的话，dp[i] = max(dp[i], dp[j] + 1)
        我们其实把 300 题可以抽象成下面这样：dp[i] 表示要求的以 0~i 子数组的状态，
        它与 ① 0~j 子数组的状态 和 ② j~i 子数组的有效性有关。即：
        dp[i] = max(dp[i], dp[j] + 1); 如果 valid(j, i)

    二、分割回文串的最少次数
        如果能把上面的递推公式想明白，那么本题也就不难了。其实只是 valid(j, i) 的区别：
        最长递增子序列中的 valid(j, i) = nums[j] < nums[i]，即 nums[j] 要小于 nums[i];
        分割回文串的最少次数的 valid(j, i) = isPalindrome(s[j + 1..i]) 即子字符串 s[j..i] 需要是回文串;
        那么与最长递增子序列类似，我们也使用动态规划，会发现两个题的状态定义和状态转移方程高度类似：

        状态定义：dp[i] 是以 i 结尾的分割成回文串的最少次数；
        状态转移方程：dp[i] = min(dp[i], dp[j] + 1);
        如果 isPalindrome(s[j + 1..i])
        现在我们分析一下，是如何得到上面的状态转移方程的。

        根据定义，dp[i] 是以 i 结尾的分割成回文串的最少次数，
        那么 dp[j] 是以 j 结尾的分割成回文串的最少次数。
        只有子字符串 s[j + 1..i] 是回文字符串的时候，
        dp[i] 可以通过 dp[j] 加上一个回文字符串 s[j + 1..i] 而得到。
        我们遍历所有的 j ∈ [0, i - 1]，dp[i] 就是所有的 s[j + 1..i] 是回文字符串的情况下，
        dp[j]的最小值 + 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii

"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        dp = [N] * N
        for i in range(N):
            if self.isPalindrome(s[0: i + 1]):
                dp[i] = 0
                continue
            for j in range(i):
                if self.isPalindrome(s[j + 1: i + 1]):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[N - 1]

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    s = "aab"
    solution = Solution()
    result = solution.minCut(s)
    print(result)
