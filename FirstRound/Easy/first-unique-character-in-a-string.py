class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        暴力解法，遍历所有元素，根据count()函数统计出现次数，等于1直接return
        不等于1将i加入list，减少后续对比次数
        没有最后返回-1
        """

        temp_list = []
        if not s.isalnum():
            return -1
        for i in s.lower():
            if i not in temp_list:
                num = s.count(i)
                if num == 1:
                    return s.index(i)
                else:
                    temp_list.append(i)
        return -1



if __name__ == '__main__':
    solution = Solution()
    index = solution.firstUniqChar(input())
    print(index)
