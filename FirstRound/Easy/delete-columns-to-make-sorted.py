"""
给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。

选取一个删除索引序列，对于 A 中的每个字符串，删除对应每个索引处的字符。 所余下的字符串行从上往下读形成列。

比如，有 A = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 A 为["bef", "vyz"]， A 的列分别为["b","v"], ["e","y"], ["f","z"]。（形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。

假设，我们选择了一组删除索引 D，那么在执行删除操作之后，A 中所剩余的每一列都必须是 非降序 排列的，然后请你返回 D.length 的最小可能值。
"""


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        """
        将对应位置的字符添加到list中，判断排序后的list是否等于原list
        不等于则加1，对应的就是需要返回的删除次数
        """
        str_len = len(A[0])
        count = 0
        for i in range(str_len):
            raw = []
            for j in range(len(A)):
                raw.append(A[j][i])
            sorted_raw = sorted(raw)
            if raw != sorted_raw:
                count += 1
        return count


if __name__ == '__main__':
    input_A = ['abc', 'hju', 'fds']
    solution = Solution()
    res = solution.minDeletionSize(input_A)
    print(res)
