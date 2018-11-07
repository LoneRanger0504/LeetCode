"""
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
"""


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        """
        count逢1下标加2，逢0加1，while循环退出条件为count >= len
        再根据count是否等于len判断，等于返回False,大于返回TRUE
        """
        bits_len = len(bits)
        count = 0
        while count < bits_len - 1:
            if bits[count] == 1:
                count += 2
            else:
                count += 1
        if count > bits_len - 1:
            return False
        elif count == bits_len - 1:
            return True


if __name__ == '__main__':
    input_list = [1, 0, 0]
    solution = Solution()
    result = solution.isOneBitCharacter(input_list)
    print(result)
