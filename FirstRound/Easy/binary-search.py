"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        就是二分查找，选择start 和 end，得到mid，判断nums[mid]是否等于target
        根据情况更新start或者end的值，注意要加减1
        循环的退出条件是start <= end
        """
        nums_len = len(nums)
        start = 0
        end = nums_len - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1


if __name__ == '__main__':
    input_list = [-1, 0, 3, 5, 9, 12]
    input_target = 9
    solution = Solution()
    res = solution.search(input_list, input_target)
    print(res)
