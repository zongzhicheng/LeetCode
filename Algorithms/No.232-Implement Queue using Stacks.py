"""
No.232：用栈实现队列
难度：简单

问题描述：

    请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
    实现 MyQueue 类：
        void push(int x) 将元素 x 推到队列的末尾
        int pop() 从队列的开头移除并返回元素
        int peek() 返回队列开头的元素
        boolean empty() 如果队列为空，返回 true ；否则，返回 false
 
说明：

    你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
    你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 
进阶：

    你能否实现每个操作均摊时间复杂度为 O(1) 的队列？
    换句话说，执行 n 个操作的总时间复杂度为 O(n) ，
    即使其中一个操作可能花费较长时间。
 
示例：

    输入：
        ["MyQueue", "push", "push", "peek", "pop", "empty"]
        [[], [1], [2], [], [], []]

    输出：
        [null, null, null, 1, 1, false]

    解释：
        MyQueue myQueue = new MyQueue();
        myQueue.push(1); // queue is: [1]
        myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
        myQueue.peek(); // return 1
        myQueue.pop(); // return 1, queue is [2]
        myQueue.empty(); // return false

提示：

    1 <= x <= 9
    最多调用 100 次 push、pop、peek 和 empty
    假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）

解题思路：

    栈：后进先出，队列：先进先出
    把一个栈当做输入栈，另一个栈当做输出栈
    当 push() 新元素的时候，放到「输入栈」的栈顶，记此顺序为「输入序」。
    当 pop() 元素的时候，是从「输出栈」弹出元素。
    如果「输出栈」为空，则把「输入栈」的元素逐个 pop() 并且 push() 到「输出栈」中，
    这一步会把「输入栈」的栈底元素放到了「输出栈」的栈顶。此时负负得正，
    从「输出栈」的 pop() 元素的顺序与「输入序」相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks

"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(2)
    obj.push(3)
    obj.push(4)
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.peek()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)
