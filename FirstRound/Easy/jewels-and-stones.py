"""
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
"""


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        """
        要做出来很简单，但是这题是哈希表的题目，如果用哈希表怎么做呢？
        就是把J里面的每个宝石类型映射到一个<j,1>的哈希表
        遍历S判断是否在哈希表的键中，再取值为1累加，
        这里都是1可以直接count，但是如果不同的宝石对应不同的权重，就要用哈希表
        """
        count = 0
        for i in J:
            count += S.count(i)
        return count


if __name__ == '__main__':
    input_J = 'aA'
    input_S = 'aAAAbbb'
    solution = Solution()
    result = solution.numJewelsInStones(input_J, input_S)
    print(result)
