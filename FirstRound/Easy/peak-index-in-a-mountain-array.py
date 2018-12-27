"""
我们把符合下列属性的数组 A 称作山脉：

A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。
"""


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        最直观的想法就是遍历，找到一个数，使他与前一个数的差和后一个数与他的差的乘积小于0
        但是这道题明确说明存在峰顶，其实就是数组的最大值，直接返回下标即可
        但是但是，遍历的方法时间复杂度是O(N)，还可以使用二分查找来找最大值，复杂度为O(logN)
        """
        for i in range(1, len(A) - 1):
            if (A[i] - A[i - 1]) * (A[i + 1] - A[i]) < 0:
                return i


if __name__ == '__main__':
    input_list = [1, 2, 3, 2]
    solution = Solution()
    res = solution.peakIndexInMountainArray(input_list)
