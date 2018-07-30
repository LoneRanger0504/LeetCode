class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        if x_str[0] == '-':
            x_rev = '-' + x_str[:0:-1]
        else:
            x_rev = x_str[::-1]
        x_reverse = int(x_rev)
        if x_reverse < -(2 ** 31) or x_reverse > (2 ** 31) - 1:
            return 0
        else:
            return x_reverse


if __name__ == '__main__':
    x = input()
    solution = Solution()
    reverse_num = solution.reverse(int(x))
    print(reverse_num)
