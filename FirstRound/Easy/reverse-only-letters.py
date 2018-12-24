class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        """
        先将字符串中的字母取出来倒序，再对原来字符串中的字母依次替换
        注意str不支持遍历修改，需要转成list遍历最后再join成字符串
        """
        alaphbat = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        S_len = len(S)
        s_list = list(S)
        res = []
        for i in range(S_len):
            if S[i] in alaphbat:
                res.append(S[i])
        res = res[::-1]
        count = 0
        for i in range(len(s_list)):
            if s_list[i] in alaphbat:
                s_list[i] = res[count]
                count += 1
        return ''.join(s_list)


if __name__ == '__main__':
    input_list = 'a-bC-dEf-ghIj'
    solution = Solution()
    res = solution.reverseOnlyLetters(input_list)
    print(res)
