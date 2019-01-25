"""
实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和
"""


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        """
        TODO:使用字典树遍历，可将时间复杂度降至O(len(prefix))
        """
        self.dic = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        """
        这里直接使用了dic的方法，本身的插入方法就是不存在返回空并插入，存在会覆盖
        """
        if key in self.dic.keys():
            self.dic[key] = val
        else:
            print('Null')
            self.dic[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        """
        这里也是直接遍历keys判断prefix是否是key的前len(prefix)个
        """
        count = 0
        for key in self.dic.keys():
            if prefix == key[:len(prefix)]:
                count += self.dic.get(key)
        return count

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
