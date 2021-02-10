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
