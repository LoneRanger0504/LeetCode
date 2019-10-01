"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        对strs中的每个单词，判断排序后的单词是否已经在list中
        没出现则初始化，出现过则在已有的value数组中添加当前的单词
        最后将字典所有的value添加到list中返回
        """
        if not strs:
            return []
        dic = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in dic.keys():
                dic[key] = [i]
            else:
                dic[key].append(i)
        res = list(dic.values())
        return res


if __name__ == '__main__':
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    res = solution.groupAnagrams(input_list)
    print(res)
