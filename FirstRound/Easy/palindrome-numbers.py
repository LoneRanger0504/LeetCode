class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        直接将int转为str,对str 倒序输出即可，使用str[::-1]表示从最后一个元素倒序排列
        """
        x_str = str(x)
        x_reverse = x_str[::-1]
        return x_reverse == x_str


if __name__ == '__main__':
    x = input()
    sl = Solution()
    flag = sl.isPalindrome(int(x))
    print(flag)
