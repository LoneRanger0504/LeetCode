class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        """
        使用一个dic来保存pattern与word的映射关系，
        当这种映射不是双射的时候，字典的key和value的个数是不相等的，跳出循环
        当是双射时，再根据键值对得到一个字符串，判断是否等于原word字符串，相等添加
        """
        pattern_len = len(pattern)
        res = []
        for word in words:
            if len(word) == pattern_len:
                dic = {}
                temp = ''
                for i in range(pattern_len):
                    dic[pattern[i]] = word[i]
                if len(set(dic.keys())) == len(set(dic.values())):
                    for i in pattern:
                        temp += dic.get(i)
                    if temp == word:
                        res.append(word)
                else:
                    continue
            else:
                continue
        return res


if __name__ == '__main__':
    input_list = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    input_pattern = "abb"
    solution = Solution()
    res = solution.findAndReplacePattern(input_list, input_pattern)
    print(res)
