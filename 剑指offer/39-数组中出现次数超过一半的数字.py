# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        """
        :param numbers:
        :return:
        """
        """
        (1)哈希表存储加判断,时间复杂度O(N)，空间复杂度O(N)
        (2)Partition函数，类似快排思路，时间复杂度O(N)，空间复杂度O(1)，但是会修改原数组
        (3)根据数组特点只使用一个额外常数指针，时间复杂度O(N)，空间复杂度O(1)，且不修改原数组
        """
        #  1.Hash
        # if not numbers:
        #     return 0
        # count = len(numbers) / 2
        # dic = {}
        # for num in numbers:
        #     if num not in dic.keys():
        #         dic[num] = 1
        #     else:
        #         dic[num] = dic.get(num) + 1
        #     if dic.get(num) > count:
        #         return num
        # return 0
        #  2.Partition函数
        #  待补充
        #  3.常数指针
        if not numbers:
            return 0

        def isValid(numbers):
            target = len(numbers) / 2
            dic = {}
            max_count = float('-inf')
            for num in numbers:
                if num not in dic.keys():
                    dic[num] = 1
                else:
                    dic[num] = dic.get(num) + 1
            for key in dic.keys():
                if dic.get(key) > max_count:
                    max_count = dic.get(key)
            return max_count > target

        res = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if count == 0:
                res = numbers[i]
                count = 1
            elif numbers[i] == res:
                count += 1
            else:
                count -= 1

        return res if isValid(numbers) else 0


if __name__ == '__main__':
    input_numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    solution = Solution()
    res = solution.MoreThanHalfNum_Solution(input_numbers)
    print(res)
