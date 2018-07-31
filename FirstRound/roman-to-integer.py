class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        roman_dic = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        j = 0
        # list = []
        s_len = len(s)
        for i in range(s_len):
            x = max(i, j)
            if x < s_len - 1:
                if roman_dic[s[x]] >= roman_dic[s[x + 1]]:
                    result += roman_dic[s[x]]
                    # list.append(s[x])
                    j += 1
                else:
                    result += roman_dic[s[x + 1]] - roman_dic[s[x]]
                    # list.append(s[x]+s[x+1])
                    j += 2
            elif x == s_len - 1:
                result += roman_dic[s[s_len - 1]]
                # list.append(s[s_len - 1])
                break
            else:
                break
        # for res in list:
        #     result += roman_dic[res]
        return result
        # print(result)


if __name__ == '__main__':
    s = input()
    solution = Solution()
    num = solution.romanToInt(s)
    print(num)
