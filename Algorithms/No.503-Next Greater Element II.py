"""
No.503：下一个更大元素 II
难度：中等

问题描述：

    给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
    数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，
    这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

    输入: [1,2,1]

    输出: [2,-1,2]

    解释: 第一个 1 的下一个更大的数是 2；
    数字 2 找不到下一个更大的数；
    第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

    注意: 输入数组的长度不会超过 10000。

解题思路：

    如果直接暴力求解，对于每个元素都向后去寻找比它大的元素，那么时间复杂度为O(N^2)会超时
    采用单调栈，对原数组遍历一次，
        ·如果栈为空，则把当前元素放入栈内；
        ·如果栈不为空，则需要判断当前元素和栈顶元素的大小：
            ·如果当前元素比栈顶元素大：说明当前元素是前面一些元素的「下一个更大元素」，
            则逐个弹出栈顶元素，直到当前元素比栈顶元素小为止。
            ·如果当前元素比栈顶元素小：说明当前元素的「下一个更大元素」与栈顶元素相同，则把当前元素入栈。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii

"""


def nextGreaterElements(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    N = len(nums)
    res = [-1] * N
    stack = []
    for i in range(N * 2):
        while stack and nums[stack[-1]] < nums[i % N]:
            res[stack.pop()] = nums[i % N]
        # 栈里面需要保存元素在数组中的下标，而不是具体的数字。
        # 所以需要根据下标修改结果数组 res
        stack.append(i % N)
    return res


if __name__ == '__main__':
    nums = [1, 2, 1]
    result = nextGreaterElements(nums)
    print(result)
