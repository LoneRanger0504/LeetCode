"""
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。

注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        """
        思路解法都同297二叉树的序列化与反序列化
        """

        def dfs(root):
            if not root:
                s.append('$')
                return
            s.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return root

        s = []
        if not root:
            s.append('$')
            return ''.join(s)
        dfs(root)
        print(s)
        return ''.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def deserialize_helper(array):
            if not array:
                return
            val = array.pop(0)
            if val == '$':
                return
            root = TreeNode(val)
            root.left = deserialize_helper(array)
            root.right = deserialize_helper(array)
            return root

        print(data)
        node_list = data.split(',')
        return deserialize_helper(node_list)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    codec = Codec()
    codec.deserialize(codec.serialize(root))
