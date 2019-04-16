"""
给定两个字符串, A 和 B。
A 的旋转操作就是将 A 最左边的字符移动到最右边。
例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。
如果在若干次旋转操作之后，A 能变成B，那么返回True。
"""


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        """
        A经过n次旋转后能否得到B
        简单做法： return B in A+A
        """
        if A == B:
            return True
        if len(A) != len(B) or not A or not B:
            return False

        b_list = [i for i in B]

        for i in range(len(A)):
            a_list = [s for s in A]
            ahead = a_list[:i]
            behind = a_list[i:]
            reverse = behind + ahead
            if reverse == b_list:
                return True
        return False


if __name__ == '__main__':
    input_A = 'abcde'
    input_B = 'cdeab'
    solution = Solution()
    res = solution.rotateString(input_A, input_B)
    print(res)
