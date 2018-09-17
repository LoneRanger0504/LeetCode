class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        第一遍思路：
        还是将int转为str，判断是否以-号开头，如果是，将str从最后一个元素到第二个元素倒序输出加上负号
        如果是正数，直接倒序输出，同时判断反转后的数有没有溢出，超过32bit的表示范围（-2^31~2^31-1）则返回0
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
