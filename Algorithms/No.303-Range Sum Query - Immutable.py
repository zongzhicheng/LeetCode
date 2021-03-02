"""
No.303：区域和检索 - 数组不可变
难度：简单

问题描述：

    给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
    实现 NumArray 类：
    NumArray(int[] nums) 使用数组 nums 初始化对象
    int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，
    包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
     
示例：

    输入：
        ["NumArray", "sumRange", "sumRange", "sumRange"]
        [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

    输出：
        [null, 1, -1, -3]

    解释：
        NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
        numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
        numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
        numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

提示：

    0 <= nums.length <= 10^4
    -10^5 <= nums[i] <= 10^5
    0 <= i <= j < nums.length
    最多调用 10^4 次 sumRange 方法

解题思路：

    preSum（前缀和）
    假设数组长度为 N，我们定义一个长度为 N+1 的 preSum 数组，preSum[i] 表示该元素左边所有元素之和（不包含 i 元素）。
    然后遍历一次数组，累加区间 [0, i) 范围内的元素，可以得到 preSum 数组
    利用 preSum 数组，可以在 O(1) 的时间内快速求出 nums 任意区间 [i, j] (两端都包含) 的各元素之和。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable

"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        N = len(nums)
        self.preSum = [0] * (N + 1)
        for i in range(N):
            self.preSum[i + 1] = self.preSum[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.preSum[j + 1] - self.preSum[i]


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    result = obj.sumRange(2, 5)
    print(result)
