class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        先特殊后一般，如果target大于最大值或小于最小值，直接返回相应index
        如果target在list中，也直接返回index
        如果不在list中，则用二分查找来确定target的位置，定义min max mid
        根据target与mid的比较情况,改变min或max的值，当max-min=1 时，退出循环，返回max
        """
        min = 0
        max = len(nums) - 1
        mid = int((min + max) / 2)
        if target > nums[max]:
            return len(nums)
        elif target < nums[min]:
            return min
        elif target in nums:
            return nums.index(target)
        else:
            while min < max:
                if target > nums[mid]:
                    min = mid
                else:
                    max = mid
                mid = int((min + max) / 2)
                if max - min == 1:
                    return max


if __name__ == '__main__':
    num_list = [1, 3, 5, 7, 9]
    target_num = int(input())
    solution = Solution()
    index = solution.searchInsert(num_list, target_num)
    print(index)
