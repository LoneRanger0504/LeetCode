"""
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]
"""


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        """
        初始化两个指针，分别等于0和length
        从头开始遍历，遇到I将i指针加1，遇到D令d指针减1
        最后一个值等于最后的i指针
        """
        s_len = len(S)
        res = [0] * (s_len + 1)
        I_pointer = 0
        D_pointer = s_len
        for i in range(s_len):
            if S[i] == 'I':
                res[i] = I_pointer
                I_pointer += 1
            elif S[i] == 'D':
                res[i] = D_pointer
                D_pointer -= 1
        res[-1] = I_pointer
        return res


if __name__ == '__main__':
    input_s = 'DIDI'
    solution = Solution()
    res = solution.diStringMatch(input_s)
    print(res)
