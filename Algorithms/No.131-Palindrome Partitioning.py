"""
No.131：分割回文串
难度：中等

问题描述：

    给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
    回文串 是正着读和反着读都一样的字符串。

示例 1：

    输入：s = "aab"

    输出：[["a","a","b"],["aa","b"]]

示例 2：

    输入：s = "a"

    输出：[["a"]]
 
提示：

    1 <= s.length <= 16
    s 仅由小写英文字母组成

解题思路：

    回溯法的整体思路是：搜索每一条路，每次回溯是对具体的一条路径而言的。
    对当前搜索路径下的的未探索区域进行搜索，则可能有两种情况：
        1.当前未搜索区域满足结束条件，则保存当前路径并退出当前搜索；
        2.当前未搜索区域需要继续搜索，则遍历当前所有可能的选择：
        如果该选择符合要求，则把当前选择加入当前的搜索路径中，并继续搜索新的未探索区域。
    上面说的未搜索区域是指搜索某条路径时的未搜索区域，并不是全局的未搜索区域。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning

"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.isPalindrome = lambda s: s == s[::-1]
        res = []
        self.backtrack(s, res, [])
        return res

    def backtrack(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):  # 注意起始和结束位置
            if self.isPalindrome(s[:i]):
                self.backtrack(s[i:], res, path + [s[:i]])


if __name__ == '__main__':
    s = "aab"
    solution = Solution()
    result = solution.partition(s)
    print(result)
