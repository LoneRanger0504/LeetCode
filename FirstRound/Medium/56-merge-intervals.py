"""
给出一个区间的集合，请合并所有重叠的区间。
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        1.先将数组排序，保证左边的值按照从小到大排序
        2.对每个区间，判断后一个区间的左边是否在前一个区间内，即左边界是否小于前一个区间的右边界
        如果在前一个区间内，则将区间合并，加入res
        否则表示两个区间不相交，直接加入res
        """
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            pre = res[-1]
            temp = intervals[i]
            if temp[0] <= pre[1]:
                res.pop()
                res.append([min(pre[0], temp[0]), max(temp[1], pre[1])])
            else:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    input_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    solution = Solution()
    res = solution.merge(input_intervals)
    print(res)
