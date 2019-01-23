"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。
"""


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """
        一次遍历按奇偶数放到奇偶位即可，只需要先创建一个待返回的list用0填充，再替换即可
        无需使用额外的HashMap
        """
        even_index = 0
        odd_index = 1
        A_len = len(A)
        res = [0] * A_len
        for i in A:
            if i % 2 == 0:
                res[even_index] = i
                even_index += 2
            else:
                res[odd_index] = i
                odd_index += 2
        return res


if __name__ == '__main__':
    input_list = [1, 2, 4, 3]
    solution = Solution()
    res = solution.sortArrayByParityII(input_list)
