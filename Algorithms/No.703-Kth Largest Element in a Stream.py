"""
No.703：Kth Largest Element in a Stream
难度：简单

问题描述：

    设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
    请实现 KthLargest 类：
        KthLargest(int k, int[] nums)使用整数 k 和整数流 nums 初始化对象。
        int add(int val)将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。

示例：

    输入：
    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    输出：
    [null, 4, 5, 5, 8, 8]
    解释：
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);   // return 4
    kthLargest.add(5);   // return 5
    kthLargest.add(10);  // return 5
    kthLargest.add(9);   // return 8
    kthLargest.add(4);   // return 8

提示：

    1 <= k <= 104
    0 <= nums.length <= 104
    -104 <= nums[i] <= 104
    -104 <= val <= 104
    最多调用 add 方法 104 次
    题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素

解题思路：

    暴力解法：
        底层数据结构使用数组实现，当每次调用 add() 函数时，向数组添加一个元素，
        然后调用 sort() 函数，返回排序后数组的第 K 个数字。
        该做法在每次调用 add() 函数时的时间复杂度为 O(K*log(K))
    从上述解法发现，使用数组的核心问题是：数组本身不带排序功能，
    只能用 sort() 函数，导致时间复杂度过高
    因此可以考虑自带排序功能的数据结构--堆
    在大根堆中，父节点的值比每个子节点的值都要大。在小根堆中，父节点的值比每个子节点的值都要小
    本题解决步骤：
        1.使用大小为 K 的小根堆（因为我们需要在堆中保留数据流中的前 K 大元素，
        使用小根堆能保证每次调用堆的 pop() 函数时，从堆中删除的是堆中的最小的元素（堆顶）），
        在初始化的时候，保证堆中的元素个数不超过 K 。
        2.在每次 add() 的时候（调用了堆的 push() 和 pop() 方法，
        两个操作的时间复杂度都是 log(K) ），将新元素 push() 到堆中，
        如果此时堆中的元素超过了 K，那么需要把堆中的最小元素（堆顶） pop() 出来。
        3.此时堆中的最小元素（堆顶）就是整个数据流中的第 K 大元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
"""

import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]


if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    result1 = kthLargest.add(3)
    result2 = kthLargest.add(5)
    result3 = kthLargest.add(10)
    result4 = kthLargest.add(9)
    result5 = kthLargest.add(4)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
