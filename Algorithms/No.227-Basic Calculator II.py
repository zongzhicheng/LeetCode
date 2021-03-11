"""
No.227：基本计算器 II
难度：中等

问题描述：

    给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
    整数除法仅保留整数部分。

示例 1：

    输入：s = "3+2*2"

    输出：7

示例 2：

    输入：s = " 3/2 "

    输出：1

示例 3：

    输入：s = " 3+5 / 2 "

    输出：5
 
提示：

    1 <= s.length <= 3 * 10^5
    s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
    s 表示一个 有效表达式
    表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
    题目数据保证答案是一个 32-bit 整数

解题思路：

    先 *、/ 后 +、-
    使用一个栈只保存需要进行+、-运算符的所有数字（把-运算符改成负数放入栈）
    如果遇到*、/运算符，将把结果计算出来，也放到栈里
    在把所有*、/运算完成之后，最后对栈内数字求和

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii

"""


def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    stack = []
    pre_op = '+'
    num = 0
    for i, each in enumerate(s):
        # 检测字符串是否只由数字组成。
        if each.isdigit():
            num = 10 * num + int(each)
        if i == len(s) - 1 or each in "+-*/":
            if pre_op == '+':
                stack.append(num)
            elif pre_op == '-':
                stack.append(-num)
            elif pre_op == '*':
                stack.append(stack.pop() * num)
            elif pre_op == '/':
                top = stack.pop()
                if top < 0:
                    stack.append(int(top / num))
                else:
                    stack.append(top // num)
            pre_op = each
            num = 0
    return sum(stack)


if __name__ == '__main__':
    s = "14-3/2"
    result = calculate(s)
    print(result)
