"""
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
"""


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        """
        效率较低的做法是对每个数字，转成字符串，变成字符串遍历的做法，要做好几次int 和 str的转换
        但是数字题有一种技巧就是想要取一个数的每一位，只需要对这个数除以10，余数就是最后一位
        再对商继续除10，得到的余数就是倒数第二位，以此类推
        """
        # 取余
        result = []
        for i in range(left, right + 1):
            flag = 0
            Divisor = i
            while Divisor != 0:
                remainder = Divisor % 10
                quotient = (Divisor - remainder) / 10
                if remainder == 0 or i % remainder != 0:
                    flag = 1
                    break
                Divisor = quotient
            if flag == 0:
                result.append(i)
        return result

        # 转字符串
        # result = []
        # for i in range(left, right + 1):
        #     flag = 0
        #     for j in str(i):
        #         if int(j) == 0 or i % int(j) != 0:
        #             flag = 1
        #             break
        #     if flag == 0:
        #         result.append(i)
        # return result


if __name__ == '__main__':
    input_left = int(input())
    input_right = int(input())
    solution = Solution()
    result = solution.selfDividingNumbers(input_left, input_right)
    print(result)
