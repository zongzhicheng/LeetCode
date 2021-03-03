"""
No.1：两数之和
难度：简单

问题描述：

    给定一个整数数组 nums 和一个整数目标值 target，
    请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    你可以按任意顺序返回答案。

示例 1：

    输入：nums = [2,7,11,15], target = 9

    输出：[0,1]

    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：

    输入：nums = [3,2,4], target = 6

    输出：[1,2]

示例 3：

    输入：nums = [3,3], target = 6

    输出：[0,1]

提示：

    2 <= nums.length <= 10^3
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    只会存在一个有效答案

解题思路：

    使用哈希表 对于每一个x，首先查看哈希表是否存在target-x，
    然后将x插入到哈希表中，即可保证不会让x和自己匹配

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum

"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)
