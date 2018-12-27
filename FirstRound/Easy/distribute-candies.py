"""
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
"""


class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        """
        只需要判断一下总的糖果个数和糖果类别个数的关系即可
        糖果种类比总糖果数的一半多，妹妹分不到所有的糖果，最大就是总数的一半
        种类少于总数一半，可以全部分给妹妹，即最大就是所有的糖果种类
        """
        num = len(set(candies))
        candies_len = len(candies)
        if num >= candies_len // 2:
            return candies_len // 2
        else:
            return num


if __name__ == '__main__':
    input_list = [1, 1, 2, 3]
    solution = Solution()
    res = solution.distributeCandies(input_list)
