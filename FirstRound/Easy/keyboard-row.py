"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词
"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        """
        使用一个字典，同一行字母有相同的value，对字符串遍历判断，只要对应的字母的value值不相等，结束循环
        如果都相等，加入result列表返回
        但是这种手动构建字典有点蠢，可以考虑使用字符串或者set来表示
        """
        dic = {'Q': 1, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1, 'U': 1, 'I': 1, 'O': 1, 'P': 1,
               'A': 2, 'S': 2, 'D': 2, 'F': 2, 'G': 2, 'H': 2, 'J': 2, 'K': 2, 'L': 2,
               'Z': 3, 'X': 3, 'C': 3, 'V': 3, 'B': 3, 'N': 3, 'M': 3}
        result = []
        for i in words:
            flag = 0
            i_len = len(i)
            for j in range(i_len - 1):
                if dic.get(i[j + 1].upper()) != dic.get(i[j].upper()):
                    flag = 1
                    break
            if flag == 0:
                result.append(i)
        return result


if __name__ == '__main__':
    input_list = ["Hello", "Alaska", "Dad", "Peace"]
    solution = Solution()
    result = solution.findWords(input_list)
    print(result)
