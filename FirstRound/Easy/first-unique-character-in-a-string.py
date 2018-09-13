class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s.isalnum():
            return -1
        for i in s.lower():
            num = s.count(i)
            if num == 1:
                return s.index(i)


if __name__ == '__main__':
    solution = Solution()
    index = solution.firstUniqChar(input())
    print(index)
