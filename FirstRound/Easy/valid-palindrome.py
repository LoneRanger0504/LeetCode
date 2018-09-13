class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        还是使用正则表达式，匹配大小写字母或者数字，未匹配到则返回TRUE
        将匹配到的match列表中的元素拼接成字符串，进行正序和逆序遍历，得到两个list
        比较两个list是否相等
        注：最开始忘了把大小写转换放在循环外面，改为先进行小写转换，再使用列表生成式
        """
        s_lower = s.lower()
        import re
        re_pattern = '[a-zA-Z0-9]+'
        match = re.findall(re_pattern, s_lower)
        if match:
            new_str = ''.join(match)
            zhengxu = [i for i in new_str]
            nixu = [j for j in new_str[::-1]]
            return zhengxu == nixu
        else:
            return True


if __name__ == '__main__':
    # input_str = input()
    solution = Solution()
    flag = solution.isPalindrome(input())
    print(flag)
