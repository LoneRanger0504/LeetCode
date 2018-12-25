class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        1.集合做差集，使用了额外的空间
        2.只缺少一个数，用等差数列的和减去nums和：
            return n * (n + 1) // 2 - sum(nums)
        """
        list = [i for i in range(len(nums) + 1)]
        new_set = set(list)
        nums_set = set(nums)
        number = new_set - nums_set
        res = [i for i in number]
        return res[0]


if __name__ == '__main__':
    input_list = [3, 1, 2]
    solution = Solution()
    res = solution.missingNumber(input_list)
    print(res)
