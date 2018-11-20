class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """
        使用哈希表，将元素值作为键值，如果不存在，则添加<元素值，数组索引>
        如果存在，得到索引差的绝对值，如果直接小于等于k，返回TRUE
        大于k将哈希表更新，对应元素的值变为最新的索引值。
        遍历一遍数组，不满足题意则返回False
        """
        dic = {}
        for index in range(len(nums)):
            if nums[index] in dic.keys():
                res = abs(index - dic[nums[index]])
                if res <= k:
                    return True
                else:
                    dic[nums[index]] = index
            else:
                dic[nums[index]] = index
        return False


if __name__ == '__main__':
    input_list = [1, 3, 2, 4, 1, 5, 2]
    input_k = 3
    solution = Solution()
    result = solution.containsNearbyDuplicate(input_list, input_k)
    print(result)
