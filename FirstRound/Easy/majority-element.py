class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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
