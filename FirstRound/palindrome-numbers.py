class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_reverse = x_str[::-1]
        return x_reverse == x_str


if __name__ == '__main__':
    x = input()
    sl = Solution()
    flag = sl.isPalindrome(int(x))
    print(flag)
