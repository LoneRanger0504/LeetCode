class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        S_len = len(S)
        count = 0
        T_list = list(T)
        for i in S:
            if i in T:
                index = T_list.index(i)
                if count < S_len:
                    T_list[count], T_list[index] = T_list[index], T_list[count]
                    count += 1
            else:
                continue
        return ''.join(T_list)


if __name__ == '__main__':
    input_S = "cbafg"
    input_T = "abcd"
    solution = Solution()
    res = solution.customSortString(input_S, input_T)
    print(res)
