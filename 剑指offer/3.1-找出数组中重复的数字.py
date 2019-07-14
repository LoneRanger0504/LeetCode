# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
在一个长度为n的数组里所有的数字都在0~n-1范围内，数组中某些数字是重复的，但是不知道有几个数字重复了，也不知道每个数字重复了几次，请找出数组中任意一个重复的数字
输入示例： [2, 3, 1, 0, 2, 5, 3]

"""
"""
时间复杂度：O(N) 尽管代码中有一个两重循环，但是每个数字最多只需要交换2次就可以找到自己的位置，因此时间复杂度为O(N)
空间复杂度：O(1) 因为直接在原数组上进行交换，没有产生额外的空间
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
        return False


if __name__ == '__main__':
    input_nums = [2, 3, 1, 0, 2, 5, 3]
    solution = Solution()
    res = solution.duplicate(input_nums, duplication=[1, 2, 3])
    print(res)
