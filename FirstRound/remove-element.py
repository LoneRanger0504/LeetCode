class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        自己的思路还是从头遍历，对每个值判断是否等于val，不等于不动，等于直接删掉，保持下标正确就行
        中间理了半天各种毛病，总想着用当前位去和下一位比较，这样总要考虑越界问题
        """

        """
        下面这段的想法是可以的，只不过是追加到list尾部，再把前面的截掉。
        正确的思路是遍历list，不等于val，将这个值复制保存到list前部分，把后面的截掉
        """
        # nums_len = len(nums)
        # for i in range(nums_len):
        #     if nums[i] != val:
        #         nums.append(nums[i])
        # nums = nums[nums_len:]
        i = 0
        while i < len(nums) - 1:
            if nums[i] != val:
                i += 1
                continue
            else:
                nums.pop(i)
                i -= 1
            """
            这里多想了，只要等于val，删掉，让下标减一就行，不需要考虑下一位
            """
            # elif nums[i+1] != val:
            #     nums.pop(i)
            #     i -= 1
            # else:
            #     nums.pop(i+1)
            #     nums.pop(i)
            #     i -= 1
            i += 1
        """
        这里也是，不用考虑i+1就不用再多考虑最后一位了
        """
        # if len(nums) > 0 and nums[len(nums)-1] == val:
        #     nums.pop()
        return nums


if __name__ == '__main__':
    num_list = [0, 1, 2, 2, 3, 0, 4, 2]
    target_num = int(input())
    solution = Solution()
    new_len = solution.removeElement(num_list, target_num)
    print(new_len)
