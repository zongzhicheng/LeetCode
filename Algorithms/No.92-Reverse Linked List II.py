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
    head = ListNode(1)
    head.next = 2
    left = 1
    right = 1
    result = reverseBetween(head, left, right)
    print(result.val)
