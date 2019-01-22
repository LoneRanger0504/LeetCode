"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        （1）先用字典保存每个字符出现的频次，注意这里使用set去重，减少时间，记录一个max
        用遍历max来确保顺序，保证先添加出现次数少的，再添加多的到res中
        最后将res反转拼接。但是这样很慢
        （2）使用lambda表达式进行排序，temp = list(sorted(dic.items(), reverse= True, key = lambda t:t[1])
        """
        dic = {}
        res = []
        max = 0
        s_set = set(s)
        for i in s_set:
            count = s.count(i)
            if count > max: max = count
            dic[i] = count
        for i in range(max + 1):
            for key in dic.keys():
                if dic.get(key) == i:
                    temp = key * i
                    res.append(temp)
        res = res[::-1]
        return ''.join(res)


if __name__ == '__main__':
    input_s = 'eert'
    solution = Solution()
    res = solution.frequencySort(input_s)
    print(res)
