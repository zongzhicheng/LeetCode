"""
No.115：不同的子序列
难度：困难

问题描述：

    给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
    字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
    （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
    题目数据保证答案符合 32 位带符号整数范围。

示例 1：

    输入：s = "rabbbit", t = "rabbit"

    输出：3

    解释：
        如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
        (上箭头符号 ^ 表示选取的字母)
        rabbbit
        ^^^^ ^^
        rabbbit
        ^^ ^^^^
        rabbbit
        ^^^ ^^^

示例 2：

    输入：s = "babgbag", t = "bag"

    输出：5

    解释：
        如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
        (上箭头符号 ^ 表示选取的字母)
        babgbag
        ^^ ^
        babgbag
        ^^    ^
        babgbag
        ^    ^^
        babgbag
          ^  ^^
        babgbag
            ^^^
 
提示：

    0 <= s.length, t.length <= 1000
    s 和 t 由英文字母组成

解题思路：

    假设字符串 s 和 t 的长度分别为 m 和 n。
    如果 t 是 s 的子序列，则 s 的长度一定大于或等于 t 的长度，
    即只有当 m≥n 时，t 才可能是 s 的子序列。如果 m<n，则 t 一定不是 s 的子序列，因此直接返回 0。
    当 m≥n 时，可以通过动态规划的方法计算在 s 的子序列中 t 出现的个数。
    创建二维数组 dp，其中 dp[i][j] 表示在 s[i:] 的子序列中 t[j:] 出现的个数。
     # 上述表示中，s[i:] 表示 s 从下标 i 到末尾的子字符串，t[j:] 表示 t 从下标 j 到末尾的子字符串。

    · 考虑动态规划的边界情况：
        · 当 j=n 时，t[j:] 为空字符串，由于空字符串是任何字符串的子序列，
        因此对任意 0≤i≤m，有 dp[i][n]=1；
        · 当 i=m 且 j<n 时，s[i:] 为空字符串，t[j:] 为非空字符串，
        由于非空字符串不是空字符串的子序列，因此对任意 0≤j<n，有 dp[m][j]=0。
    · 当 i<m 且 j<n 时，考虑 dp[i][j] 的计算：
        · 当 s[i]=t[j] 时，dp[i][j] 由两部分组成：
            · 如果 s[i] 和 t[j] 匹配，则考虑 t[j+1:] 作为 s[i+1:] 的子序列，子序列数为 dp[i+1][j+1]；
            · 如果 s[i] 不和 t[j] 匹配，则考虑 t[j:] 作为 s[i+1:] 的子序列，子序列数为 dp[i+1][j]。
        因此当 s[i]=t[j] 时，有 dp[i][j]=dp[i+1][j+1]+dp[i+1][j]。
        · 当 s[i]≠t[j] 时，]s[i] 不能和t[j] 匹配，因此只考虑 t[j:] 作为 s[i+1:] 的子序列，
        子序列数为dp[i+1][j]。
        因此当 s[i]≠t[j] 时，有 dp[i][j]=dp[i+1][j]。
    由此可以得到如下状态转移方程：
                    / dp[i+1][j+1]+dp[i+1][j],s[i] = t[j]
        dp[i][j] =
                    \ dp[i+1][j] ,s[i] ≠ t[j]
    最终计算得到 dp[0][0] 即为在 s 的子序列中 t 出现的个数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences

"""


def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    if m < n:
        return 0

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]

    return dp[0][0]


if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    result = numDistinct(s, t)
    print(result)
