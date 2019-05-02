"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
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
        使用DFS将树进行序列化，用$表示null，同时使用 ， 进行分隔，
        返回二叉树对应的字符串表示，用于反序列化
        """

        def dfs(root):
            if not root:
                res.append('$')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return root

        res = []
        if not root:
            res.append('$')
            return ','.join(res)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        """
        还是使用前序DFS进行反序列化，先将输入的字符串转为list
        如果对应的值不为$，则新建一个树的节点，否则返回null
        反序列化生成一棵树
        """

        def dfs(node_list):
            if not node_list:
                return
            node = node_list.pop(0)
            if node == '$':
                return
            root = TreeNode(node)
            root.left = dfs(node_list)
            root.right = dfs(node_list)
            return root

        node_list = data.split(',')
        return dfs(node_list)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    codec = Codec()
    codec.deserialize(codec.serialize(root))
