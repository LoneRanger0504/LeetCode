# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
编写一个算法来判断一个数是不是“快乐数”。
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        关键问题在于如何判断无限循环并退出
        (1)快慢指针法：类似于链表有环的思路，使用快慢指针，快指针每次计算两次平方和，慢指针每次计算一次，
        如果存在循环，快指针的值会追上慢指针，但并不等于1，则返回False，如果不存在循环，快慢指针相遇时的值都为1，即表示是快乐数
        (2)使用set保存所有可能的值，如果计算出的平方和已经出现在set中，判断此时的n是否为1即可
        """

        def squareSum(num):
            square_sum = 0
            while num != 0:
                square_sum += (num % 10) * (num % 10)
                num = num // 10
            return square_sum

        #  (1)快慢指针
        # fast = squareSum(squareSum(n))
        # slow = squareSum(n)
        # while slow != fast:
        #     slow = squareSum(slow)
        #     fast = squareSum(fast)
        #     fast = squareSum(fast)
        # if fast == 1:
        #     return True
        # else:
        #     return False
        #  (2)set方法
        cycle = set()
        while n not in cycle:
            cycle.add(n)
            n = squareSum(n)
        return n == 1


if __name__ == '__main__':
    input_num = 19
    solution = Solution()
    res = solution.isHappy(input_num)
    print(res)
