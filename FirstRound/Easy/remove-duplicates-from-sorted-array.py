class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        对list直接判断，因为list是有序的，如果当前值与下一个值相等，则代表重复，删掉当前值
        注意下标正确改变，也不用单独考虑最后一位，肯定是不重复的
        但是这样是判断是否重复，增加了开销，后续改为通过不相等来判断
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)
        

if __name__ == '__main__':
    input_list = [0, 0, 1, 1, 2, 2, 2, 3, 3, 3]
    solution = Solution()
    new_len = solution.removeDuplicates(input_list)
    print(new_len)
