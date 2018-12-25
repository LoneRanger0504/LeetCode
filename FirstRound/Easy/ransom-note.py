"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
"""


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        """
        简单的判断下赎金信中的字符是否都在杂志中，且杂志中字符出现个数要大于等于赎金信
        使用set去重减少遍历次数提升速度
        """
        ransomnote_set = set(ransomNote)
        for i in ransomnote_set:
            if i not in magazine or ransomNote.count(i) > magazine.count(i):
                return False
        return True


if __name__ == '__main__':
    input_ransomNote = 'aa'
    input_magazine = 'ab'
    solution = Solution()
    res = solution.canConstruct(input_ransomNote, input_magazine)
    print(res)
