"""
No.92：反转链表 II
难度：中等

问题描述：

    给你单链表的头节点 head 和两个整数 left 和 right ，其中 left <= right 。
    请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：

    输入：head = [1,2,3,4,5], left = 2, right = 4

    输出：[1,4,3,2,5]

示例 2：

    输入：head = [5], left = 1, right = 1

    输出：[5]
 
提示：

    链表中节点数目为 n
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

解题思路：

    翻转指定区间的链表，需要以下指针：
        指向 left 左边元素的指针 pre ，它表示未翻转的链表，需要把当前要翻转的链表结点放到 pre 之后。
        cur 指向当前要翻转的链表结点。
        nxt 指向 cur.next ，表示下一个要被翻转的链表结点。
        tail 指向已经翻转的链表的结尾，用它来把已翻转的链表和剩余链表进行拼接。
    另外用到了链表题常用技巧：哑节点 dummy。
    创建 哑节点 作为 链表 的新开头，返回结果是这个节点的下一个位置。
    目的是：如果要翻转的区间包含了原始链表的第一个位置，那么使用 dummy 就可以维护整个翻转的过程更加通用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """
    count = 1
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    while pre.next and count < left:
        pre = pre.next
        count += 1
    cur = pre.next
    tail = cur
    while cur and count <= right:
        nxt = cur.next
        cur.next = pre.next
        pre.next = cur
        tail.next = nxt
        cur = nxt
        count += 1
    return dummy.next


if __name__ == '__main__':
    # 1 -> 2 -> 3 -> 4 -> 5
    listNode = ListNode(1)
    ListNode_2 = ListNode(2)
    ListNode_3 = ListNode(3)
    ListNode_4 = ListNode(4)
    ListNode_5 = ListNode(5)

    listNode.next = ListNode_2
    ListNode_2.next = ListNode_3
    ListNode_3.next = ListNode_4
    ListNode_4.next = ListNode_5

    left = 2
    right = 4
    result = reverseBetween(listNode, left, right)

    while result is not None:
        print(result.val)
        result = result.next
