"""
No.354：俄罗斯套娃信封问题
难度：困难

问题描述：

    给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
    当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
    请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
    注意：不允许旋转信封。

示例 1：

    输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]

    输出：3

    解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

示例 2：

    输入：envelopes = [[1,1],[1,1],[1,1]]

    输出：1
 
提示：

    1 <= envelopes.length <= 5000
    envelopes[i].length == 2
    1 <= wi, hi <= 10^4

解题思路：

    基于二分查找的动态规划
    设w为宽度，h为高度
    设f[j]表示 h 的前 i 个元素可以组成的长度为 j 的最长严格递增子序列的末尾元素的最小值，
    如果不存在长度为 j 的最长严格递增子序列，对应的 f 值无定义。
    在定义范围内，可以看出 f 值是严格单调递增的，因为越长的子序列的末尾元素显然越大。
    在进行状态转移时，我们考虑当前的元素hi：
        ·如果hi大于f中的最大值，那么hi就可以在f中的最大值之后，形成一个长度最长的严格递增子序列；
        ·否则我们找出f中比hi严格小的最大的元素f[j0]，即f[j0]<hi<=f[j0+1]进行更新：
            f[j0+1]=hi
        我们可以在f上进行二分查找，找出满足要求的j0
    在遍历所有的hi之后，f中最后一个有定义的元素的下标增加 1（下标从 0 开始）即为最长严格递增子序列的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/russian-doll-envelopes

"""
import bisect


def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    if not envelopes:
        return 0

    n = len(envelopes)
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    f = [envelopes[0][1]]
    for i in range(1, n):
        if (num := envelopes[i][1]) > f[-1]:
            f.append(num)
        else:
            index = bisect.bisect_left(f, num)
            f[index] = num

    return len(f)


if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    result = maxEnvelopes(envelopes)
