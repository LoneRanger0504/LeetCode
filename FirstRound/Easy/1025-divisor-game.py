# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
"""


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        """
        爱丽丝先手的情况下，是偶数就必赢，奇数必输，记得使用位运算代替模2运算
        """
        return not N & 1


if __name__ == '__main__':
    input_N = 3
    solution = Solution()
    res = solution.divisorGame(input_N)
    print(res)
