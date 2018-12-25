"""
你有一个日志数组 logs。每条日志都是以空格分隔的字串。

对于每条日志，其第一个字为字母数字标识符。然后，要么：

标识符后面的每个字将仅由小写字母组成，或；
标识符后面的每个字将仅由数字组成。
我们将这两种日志分别称为字母日志和数字日志。保证每个日志在其标识符后面至少有一个字。

将日志重新排序，使得所有字母日志都排在数字日志之前。字母日志按字母顺序排序，忽略标识符，标识符仅用于表示关系。数字日志应该按原来的顺序排列。

返回日志的最终顺序。
"""


class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        """
        按照字母或数字进行分类，数字直接添加到一个数组
        字母需要进行排序，最后和数字数组相加即可。
        但是在排序这里，可以使用lambda表达式从第2项开始排序(这里使用了比较蠢的分割再拼接的做法,用字典存储待排序字符与其对应的标识符，注意字典的key值必须不可变，因此可以是字符串)
        对字母数组：
            alphabat = sorted(alphabat, key = lambda x:x.split()[1:])
        """
        alphabat = []
        number = []
        dic = {}
        for log in logs:
            log_list = log.split(' ')
            title = log_list[0]
            if log_list[1][0].isalpha():
                word_list = log_list[1:]
                word = ' '.join(word_list)
                dic[word] = title
                alphabat.append(word)
            else:
                number.append(log)
        alphabat.sort()
        for i in range(len(alphabat)):
            alphabat[i] = dic.get(alphabat[i]) + ' ' + alphabat[i]
        res = alphabat + number
        return res


if __name__ == '__main__':
    input_list = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    solution = Solution()
    res = solution.reorderLogFiles(input_list)
    print(res)
