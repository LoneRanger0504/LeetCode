"""
你和你的朋友，两个人一起玩 Nim游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。

你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
"""


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        巴什博弈，最多取n个情况下， n % (m + 1) != 0 时先手必胜
        """
        return n % 4 != 0


if __name__ == '__main__':
    input_n = 4
    solution = Solution()
    res = solution.canWinNim(input_n)
    print(res)
