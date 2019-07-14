# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) <= 0:
            return 0
        start = 0
        end = len(rotateArray) - 1
        mid = start
        while rotateArray[start] >= rotateArray[end]:
            if end - start == 1:
                mid = end
                break
            mid = (start + end) >> 1
            #  在这里增加了一个如果有重复数字的判断，如果start， mid， end三个值都相等，只能顺序查找最小值
            if rotateArray[start] == rotateArray[end] and rotateArray[start] == rotateArray[mid]:
                return min(rotateArray[start + 1:end])
            if rotateArray[mid] >= rotateArray[start]:
                start = mid
            elif rotateArray[mid] <= rotateArray[end]:
                end = mid
        return rotateArray[mid]


if __name__ == '__main__':
    input_rotateArray = [1, 0, 1, 1, 1, 1, 1]
    solution = Solution()
    res = solution.minNumberInRotateArray(input_rotateArray)
    print(res)
