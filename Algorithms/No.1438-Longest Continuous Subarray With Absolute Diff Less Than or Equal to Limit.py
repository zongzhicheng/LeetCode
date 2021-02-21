"""
No.1438：绝对差不超过限制的最长连续子数组
难度：中等

问题描述：

    给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
    如果不存在满足条件的子数组，则返回 0 。

示例 1：

    输入：nums = [8,2,4,7], limit = 4

    输出：2

    解释：所有子数组如下：
        [8] 最大绝对差 |8-8| = 0 <= 4.
        [8,2] 最大绝对差 |8-2| = 6 > 4.
        [8,2,4] 最大绝对差 |8-2| = 6 > 4.
        [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
        [2] 最大绝对差 |2-2| = 0 <= 4.
        [2,4] 最大绝对差 |2-4| = 2 <= 4.
        [2,4,7] 最大绝对差 |2-7| = 5 > 4.
        [4] 最大绝对差 |4-4| = 0 <= 4.
        [4,7] 最大绝对差 |4-7| = 3 <= 4.
        [7] 最大绝对差 |7-7| = 0 <= 4.
        因此，满足题意的最长子数组的长度为 2 。

示例 2：

    输入：nums = [10,1,2,4,7,2], limit = 5

    输出：4

    解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。

示例 3：

    输入：nums = [4,2,2,2,4,4,2,2], limit = 0

    输出：3
 

提示：

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= limit <= 10^9

解题思路：

    使用滑动窗口，使用 left 和 right 两个指针，分别指向滑动窗口的左右边界；
    定义 multiset 保存滑动窗口的所有元素；
    right 主动右移：right 指针每次移动一步，把 A[right] 放入滑动窗口
    left 被动右移：判断此时窗口内最大值和最小值的差，如果大于 limit，则 left 指针被迫右移，
    直至窗口内最大值和最小值的差小于等于 limit 为止；
    left 每次右移之前，需要把 A[left] 从 multiset 中减去一次。
    滑动窗口长度的最大值就是所求。
    主要难点在于快速求滑动窗口的最大最小值，这里采用平衡二叉搜索树。
    插入元素会自动调整二叉树，使得每个子树根节点的键值大于左子树所有节点的键值，
    同时保证根节点左右子树的高度相等，这样二叉树高度最小，检索速度最快。
    它的中序遍历是有序的，另外它也允许出现重复的值
    时间复杂度O(N*log(N))，每个元素遍历一次，新元素遍历红黑树的调整时间为O(log(N))
    空间复杂度O(N)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

"""


def longestSubarray(nums, limit):
    """
    :type nums: List[int]
    :type limit: int
    :rtype: int
    """
    from sortedcontainers import SortedList
    s = SortedList()
    left, right = 0, 0
    res = 0
    while right < len(nums):
        s.add(nums[right])
        while s[-1] - s[0] > limit:
            s.remove(nums[left])
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res


if __name__ == '__main__':
    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    result = longestSubarray(nums, limit)
    print(result)
