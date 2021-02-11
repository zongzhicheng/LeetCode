"""
No.567：字符串的排列
难度：中等

问题描述：

    给定两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。
    换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

    输入: s1 = "ab" s2 = "eidbaooo"
    输出: True
    解释: s2 包含 s1 的排列之一 ("ba").
 
示例2:

    输入: s1= "ab" s2 = "eidboaoo"
    输出: False
 
注意：

    输入的字符串只包含小写字母
    两个字符串的长度都在 [1,10000] 之间

解题思路：

    分析：
        1.题目要求 s1 的排列之一是 s2 的一个子串,而子串必须是连续的，
        所以要求的 s2 子串的长度跟 s1 长度必须相等。
        2.如果字符串 a 是 b 的一个排列，那么当且仅当它们两者中的每个字符的个数都必须完全相等。
    我们使用一个和 s1 长度相等的固定窗口大小的滑动窗口，在 s2 上面从左向右滑动，
    判断 s2 在滑动窗口内的每个字符出现的个数是否跟 s1 每个字符出现次数完全相等。
    定义 counter1 是对 s1 内字符出现的个数的统计，定义 counter2 是对 s2 内字符出现的个数的统计。
    在窗口每次右移的时候，需要把右边新加入窗口的字符个数在 counter2 中加 1，把左边移出窗口的字符的个数减 1。
    如果 counter1 == counter2 ，那么说明窗口内的子串是 s1 的一个排列，返回 True
    如果窗口已经把 s2 遍历完了仍然没有找到满足条件的排列，返回 False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string

"""

import collections


def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    # 统计 s1 中每个字符出现的次数
    counter1 = collections.Counter(s1)
    N = len(s2)
    # 定义滑动窗口的范围是 [left, right]，长度与s1相等
    left = 0
    right = len(s1) - 1
    # 统计窗口s2[left, right - 1]内的元素出现的次数
    counter2 = collections.Counter(s2[0:right])
    while right < N:
        # 把 right 位置的元素放到 counter2 中
        counter2[s2[right]] += 1
        # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
        if counter1 == counter2:
            return True
        # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
        counter2[s2[left]] -= 1
        # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
        if counter2[s2[left]] == 0:
            del counter2[s2[left]]
        # 窗口向右移动
        left += 1
        right += 1
    return False


if __name__ == '__main__':
    result1 = checkInclusion("ab", "eidbaooo")
    result2 = checkInclusion("ad", "eidbaooo")
    print(result1)
    print(result2)
