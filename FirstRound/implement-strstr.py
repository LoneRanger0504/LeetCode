class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        直接使用str自带的index进行判断，后续改通过更基础方法实现
        """
        if needle == '':
            return 0
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


if __name__ == '__main__':
    haystack_str = input()
    needle_str = input()
    solution = Solution()
    index = solution.strStr(haystack_str, needle_str)
    print(index)
