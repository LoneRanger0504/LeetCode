class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        第一遍没做出来，不合适的思路：
        遍历列表中的每个元素，依次取其第j位字符对比，如果直接不相等，直接跳出循环，返回空串；
        如果相等，依次循环遍历，直到退出，但是要判断是否是最后一位以及最后如何返回公共前缀
        正确思路待补充：
        """


if __name__ == '__main__':
    list1 = ["flower", "flow", "flight"]
    list2 = ["dog", "racecar", "car"]
    solution = Solution()
    common_prefix = solution.longestCommonPrefix(list2)
    print(common_prefix)
