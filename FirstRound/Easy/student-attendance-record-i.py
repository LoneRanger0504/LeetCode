"""
给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤纪录判断他是否会被奖赏
"""


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        判断A和L的数量，先判断A的数量，再直接判断LLL是否在字符串中
        但是有点混乱，应该将TRUE与FALSE的条件整合，改为：
        if s.count('A') <=1 and 'LLL' not in s:
            return True
        else: return False
        """
        if s.count('A') > 1:
            return False
        elif s.count('L') < 3:
            return True
        else:
            for i in range(0, len(s) - 2):
                if s[i] == 'L' and s[i + 1] == 'L' and s[i + 2] == 'L':
                    return False
            return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.checkRecord(input())
    print(result)
