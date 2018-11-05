"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        判断条件很简单，就是出现次数大于长度一半，这里默认肯定存在一个众数（未考虑多个众数情况）
        使用了一个新的list存储重复元素，使每个元素只判断一次，节省时间
        """
        cache_list = []
        nums_len = len(nums)
        half_len = int(nums_len / 2)
        for i in nums:
            if i not in cache_list:
                cache_list.append(i)
                count = nums.count(i)
                if count > half_len:
                    return i
                else:
                    continue
            else:
                continue


if __name__ == '__main__':
    input_list = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    result = solution.majorityElement(input_list)
