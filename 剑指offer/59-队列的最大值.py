"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
{2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res = []
        if len(num) >= size and size >= 1:
            index = []
            for i in range(size):
                while index and num[i] >= num[index[-1]]:
                    index.pop()
                index.append(i)
            for i in range(size, len(num)):
                res.append(num[index[0]])
                while index and num[i] >= num[index[-1]]:
                    index.pop()
                if index and index[0] <= i - size:
                    index.pop(0)
                index.append(i)
            res.append(num[index[0]])
        return res


if __name__ == '__main__':
    input_num = [2, 3, 4, 2, 6, 2, 5, 1]
    input_size = 3
    solution = Solution()
    res = solution.maxInWindows(input_num, input_size)
    print(res)