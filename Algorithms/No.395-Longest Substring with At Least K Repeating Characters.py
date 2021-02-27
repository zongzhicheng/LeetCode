"""
No.395：至少有 K 个重复字符的最长子串
难度：中等

问题描述：

    给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串，
    要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

示例 1：

    输入：s = "aaabb", k = 3

    输出：3

    解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。

示例 2：

    输入：s = "ababbc", k = 2

    输出：5

    解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
 
提示：

    1 <= s.length <= 10^4
    s 仅由小写英文字母组成
    1 <= k <= 10^5

解题思路：

    递归：
        如果一个字符c在s中出现的次数少于k次，那么s中所有的包含c的子字符串都不能满足题意。
        所以，应该在s的所有不包含c的子字符串中继续寻找结果：
            把s按照c分割（分割后每个子串都不包含c），得到很多子串t；
            下一步要求t作为源字符串的时候，它的最长的满足题意的子字符串长度。
        如果s中的每个字符出现的次数都大于k次，那么s就是我们要求的字符串，直接返回字符串的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters

"""


def longestSubstring(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if len(s) < k:
        return 0
    for c in set(s):
        if s.count(c) < k:
            return max(longestSubstring(t, k) for t in s.split(c))
    return len(s)


if __name__ == '__main__':
    s = "ababbc"
    k = 2
    result = longestSubstring(s, k)
    print(result)
