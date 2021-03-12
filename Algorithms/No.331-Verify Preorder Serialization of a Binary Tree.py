"""
No.331：验证二叉树的前序序列化
难度：中等

问题描述：

    序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。
    如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
         _9_
        /   \
       3     2
      / \   / \
     4   1 #  6
    / \ / \  / \
    # # # #  #  #
    例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
    给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
    每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
    你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1：

    输入："9,3,4,#,#,1,#,#,2,#,6,#,#"

    输出：true

示例 2：

    输入："1,#"

    输出：false

示例 3：

    输入："9,#,#,1"

    输出：false

解题思路：

    前序遍历：根节点-左子树-右子树
    方法一：栈

        本题可以先判断左子树是否有效，再判断右子树是否有效，最后判断根节点-左子树-右子树是否有效
        如果判断是否有效？首先考虑最简单的：叶子节点，当一个节点的两个孩子均为#的时候，该节点就是叶子节点
        当一个节点不是叶子节点的时候，那么必定有一个孩子非空！
        本题可以采用如下技巧，
            把有效的叶子节点使用 "#" 代替，比如把 4## 替换成 #。此时，非叶子节点会变成叶子节点！
        比如：9,3,4,#,#,1,#,#,2,#,6,#,#
            9,3,4,#,# => 9,3,#，继续
            9,3,#,1,#,# => 9,3,#,# => 9,# ，继续
            9,#2,#,6,#,# => 9,#,2,#,# => 9,#,# => #，结束
        代码如 isValidSerialization1(preorder)

    方法二：入度出度

        树的所有入度之和等于出度之和
        在一棵二叉树中：
            每个#会提供 0 个出度和 1 个入度。
            每个非空节点会提供 2 个出度和 1 个入度。
        我们只要把字符串遍历一次，每个节点都累加 diff = 出度 - 入度 。
        在遍历到任何一个节点的时候，要求diff >= 0，
        原因是还没遍历到该节点的子节点，所以此时的出度应该大于等于入度。
        当所有节点遍历完成之后，整棵树的 diff == 0 。
        diff 的初始化为 1。因为，我们加入一个非空节点时，
        都会先减去一个入度，再加上两个出度。
        但是由于根节点没有父节点，所以其入度为 0，出度为 2。
        因此 diff 初始化为 1，是为了在加入根节点的时候，先减去一个入度，再加上两个出度，
        此时 diff 正好应该是2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree

"""


def isValidSerialization1(preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    stack = []
    for node in preorder.split(','):
        stack.append(node)
        while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
            stack.pop(), stack.pop(), stack.pop()
            stack.append('#')
    return len(stack) == 1 and stack.pop() == '#'


def isValidSerialization2(preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    nodes = preorder.split(',')
    diff = 1
    for node in nodes:
        diff -= 1
        if diff < 0:
            return False
        if node != '#':
            diff += 2
    return diff == 0


if __name__ == '__main__':
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    result1 = isValidSerialization1(preorder)
    result2 = isValidSerialization2(preorder)
    print(result1)
    print(result2)
