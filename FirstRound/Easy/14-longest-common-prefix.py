"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        第一遍没做出来，不合适的思路：
        遍历列表中的每个元素，依次取其第j位字符对比，如果直接不相等，直接跳出循环，返回空串；
        如果相等，依次循环遍历，直到退出，但是要判断是否是最后一位以及最后如何返回公共前缀
        正确思路待补充：
        第二遍的思路：公共前缀的长度最大其实也就是数组中长度最短的字符串的长度，
        先一遍遍历找到长度最短的字符串对应的位置，以他为标杆，再进行遍历
        如果某个字符串的某一位和最短字符串的对应位相同，继续循环，直到所有的字符串的第i位都相同，加到公共前缀中
        否则只要中间有一位不同，直接返回当前的最长公共前缀
        """
        max_common_prefix = ''
        if not strs:
            return max_common_prefix
        #  遍历找到最短的字符串及其下标
        min_len = 100000
        index = 0
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                index = i
        #  遍历strs，一旦出现每个字符串的某一位有不同，则直接返回当前的最长公共前缀
        for i in range(len(strs[index])):
            for j in range(len(strs) - 1):
                if strs[j][i] == strs[j + 1][i]:
                    continue
                else:
                    return max_common_prefix
            max_common_prefix += strs[index][i]
        return max_common_prefix


if __name__ == '__main__':
    list1 = ["flower", "flow", "flight"]
    list2 = ["aca", "cba"]
    solution = Solution()
    common_prefix = solution.longestCommonPrefix(list2)
    print(common_prefix)
