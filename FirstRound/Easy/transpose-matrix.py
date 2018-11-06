class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        先创建一个转置好的矩阵B，防止在原数组上变换出现越界
        然后将元素转置放到对应的位置即可。
        但是有一种更简洁的解法：return list(map(list,zip(*A)))
        zip函数是python的一个内建函数。它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），
        然后返回由这些tuples组成的list（列表）。
        若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
        利用*号操作符，可以将list unzip（解压）
        """
        M = len(A)
        N = len(A[0])
        B = [None] * N
        for i in range(len(B)):
            B[i] = [0] * M

        for i in range(len(A)):
            for j in range(len(A[i])):
                B[j][i] = A[i][j]
        return B


if __name__ == '__main__':
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    result = solution.transpose(input_list)
    print(result)
