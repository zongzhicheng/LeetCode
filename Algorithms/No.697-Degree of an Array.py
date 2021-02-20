"""
No.697：数组的度
难度：简单

问题描述：

    给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
    你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1：

    输入：[1, 2, 2, 3, 1]

    输出：2

    解释：输入数组的度是2，因为元素1和2的出现频数最大，均为2。
    连续子数组里面拥有相同度的有如下所示:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    最短连续子数组[2, 2]的长度为2，所以返回2。

示例 2：

    输入：[1,2,2,3,1,4,2]

    输出：6

提示：

    nums.length 在 1 到 50,000 区间范围内。
    nums[i] 是一个在 0 到 49,999 范围内的整数。

解题思路：

    · 先求原数组的度
         counter 计数
         数组的度 degree 等于 counter.values() 的最大值；
    · 再求与原数组相同度的最短子数组
        left , right 保存每个元素在数组中第一次出现的位置和最后一次出现的位置
        对counter再次遍历:
            如果元素 k 出现的次数等于 degree，则找出元素 k 最后一次出现的位置 和 第一次出现的位置,
            计算两者之差+1，即为子数组长度.对所有出现次数等于 degree 的子数组的最短长度，取 min

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array

"""
import collections


def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 记录每个数在数组出现最左的和最右的位置
    left, right = dict(), dict()
    # 计算每个数的频数
    counter = collections.Counter()
    for i, num in enumerate(nums):
        if num not in left:
            left[num] = i
        right[num] = i
        counter[num] += 1
    # 数组的度
    degree = max(counter.values())
    res = len(nums)
    for k, v in counter.items():
        if v == degree:
            res = min(res, right[k] - left[k] + 1)
    return res


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1, 4, 2]
    result = findShortestSubArray(nums)
    print(result)
