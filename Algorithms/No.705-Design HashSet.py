"""
No.705：设计哈希集合
难度：简单

问题描述：

    不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
    实现 MyHashSet 类：
        · void add(key) 向哈希集合中插入值 key 。
        · bool contains(key) 返回哈希集合中是否存在这个值 key 。
        · void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
 
示例：

    输入：
    ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]

    输出：
    [null, null, null, true, false, null, true, null, false]

    解释：
        MyHashSet myHashSet = new MyHashSet();
        myHashSet.add(1);      // set = [1]
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(1); // 返回 True
        myHashSet.contains(3); // 返回 False ，（未找到）
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(2); // 返回 True
        myHashSet.remove(2);   // set = [1]
        myHashSet.contains(2); // 返回 False ，（已移除）
 
提示：

    0 <= key <= 10^6
    最多调用 10^4 次 add、remove 和 contains 。

解题思路：

    HashSet是在时间和空间上做权衡的经典例子：
        如果不考虑空间，我们可以直接设计一个超大的数组，使每个key 都有单独的位置，则不存在冲突；
        如果不考虑时间，我们可以直接用一个无序的数组保存输入，每次查找的时候遍历一次数组。
    拉链法：
        我们定义了一个比较小的数组，然后使用hash方法来把求出 key 应该出现在数组中的位置；
        但是由于不同的 key 在求完 hash 之后，可能会存在碰撞冲突，所以数组并不直接保存元素，
        而是每个位置都指向了一条链表（或数组）用于存储元素。
        我们可以看出在查找一个 key 的时候需要两个步骤：
            ① 求hash到数组中的位置；
            ② 在链表中遍历找key。
        优点：我们可以把数组大小设计比较合理，从而节省空间；不用预知 key 的范围；方便扩容。
        缺点：需要多次访问内存，性能上比超大数组的 HashSet 差；需要设计合理的 hash 方法实现均匀散列；
        如果链表比较长，则退化成 O(N) 的查找；实现比较复杂；
    不定长的拉链数组
        是说拉链会根据分桶中的 key 动态增长，更类似于真正的链表。
        分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。
        优点：节省内存，不用预知数据范围；
        缺点：在链表中查找元素需要遍历。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-hashset

"""


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hashkey = self.hash(key)
        return key in self.table[hashkey]


if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    obj.remove(3)
    result = obj.contains(3)
    print(result)
