"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k < 0 or k > len(tinput):
            return []
        def quick_sort(input):
            if not input:
                return []
            pivot = input[0]
            left = quick_sort([x for x in input[1:] if x < pivot])
            right = quick_sort([x for x in input[1:] if x > pivot])
            return left + [pivot] + right
        res = quick_sort(tinput)
        return res[:k]


if __name__ == '__main__':
    tinput = [4, 5, 1, 6, 2, 7, 3, 8]
    k = 4
    solution = Solution()
    res = solution.GetLeastNumbers_Solution(tinput, k)
    print(res)