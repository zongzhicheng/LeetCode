"""
No.1052：爱生气的书店老板
难度：中等

问题描述：

    今天，书店老板有一家店打算试营业 customers.length 分钟。
    每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
    在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
    当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
    书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
    请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
 
示例：

    输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3

    输出：16

    解释：
        书店老板在最后 3 分钟保持冷静。
        感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 
提示：

    1 <= X <= customers.length == grumpy.length <= 20000
    0 <= customers[i] <= 1000
    0 <= grumpy[i] <= 1

解题思路：

    · 所有不生气时间内的顾客总数：使用 i 遍历[0, customers.length)
    累加 grumpy[i] == 0 时的 customers[i]
    · 在窗口 X 内因为生气而被赶走的顾客数：使用大小为 X 的滑动窗口，
    计算滑动窗口内的 grumpy[i] == 1 时的 customers[i] ，
    得到在滑动窗口内老板生气时对应的顾客数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner

"""


def maxSatisfied(customers, grumpy, X):
    """
    :type customers: List[int]
    :type grumpy: List[int]
    :type X: int
    :rtype: int
    """
    N = len(customers)
    # 所有不生气时间的顾客总数
    sum = 0
    for i in range(N):
        sum += customers[i] * (1 - grumpy[i])
    # 生气的X分钟内，会让多少顾客不满意
    curValue = 0
    for i in range(X):
        curValue += customers[i] * grumpy[i]
    resValue = curValue

    # 然后利用滑动窗口，每次向右移动一步
    for i in range(X, N):
        # 如果新进入窗口的元素是生气的，累加不满意的顾客到滑动窗口中
        # 如果离开窗口的元素是生气的，则从滑动窗口中减去该不满意的顾客数
        curValue = curValue + customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
        # 求所有窗口内不满意顾客的最大值
        resValue = max(resValue, curValue)
    # 最终结果是：不生气时的顾客总数 + 窗口X内挽留的因为生气被赶走的顾客数
    return sum + resValue


if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    result = maxSatisfied(customers, grumpy, X)
    print(result)
