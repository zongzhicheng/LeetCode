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
