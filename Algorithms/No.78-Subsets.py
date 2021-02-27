"""
No.78：子集
难度：中等

问题描述：

    给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
    解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：

    输入：nums = [1,2,3]

    输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：

    输入：nums = [0]

    输出：[[],[0]]
 
提示：

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    nums 中的所有元素 互不相同

解题思路：

    直接遍历，遇到一个数就把所有加上该数组成新的子集，遍历完即是所有子集

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets

"""


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = subsets(nums)

