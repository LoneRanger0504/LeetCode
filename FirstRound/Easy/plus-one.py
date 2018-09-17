class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        """
        最暴力的解法，遍历列表元素先拼接成字符串，字符串转整数加1，
        再转成字符串依次添加到新的list，后续待优化
        """
        """
        以后要考虑效率优化
        （1）多考虑使用列表生成式代替循环添加
        （2）使用.join方法代替 + 实现字符串拼接
        （3）避免在循环中使用func(i),在列表生成式中使用，再进行拼接
        """
        # num = ''
        num_list = [str(i) for i in digits]
        num = ''.join(num_list)
        # for i in digits:
        #     num += str(i)

        result = int(num) + 1

        return_list = [int(j) for j in str(result)]
        # for j in str(result):
        #     return_list.append(int(j))

        return return_list


if __name__ == '__main__':
    input_list = [1, 2, 3, 9]
    solution = Solution()
    output_list = solution.plusOne(input_list)
    print(output_list)
