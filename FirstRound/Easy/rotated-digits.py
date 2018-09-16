"""
我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
N 的取值范围是 [1, 10000]。
"""


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        暴力解法，构建一个词典，对应有效的旋转值
        对1-N内的数，变成str类型，如果这个数的每一位都是有效旋转，flag=TRUE，新的字符串等于旋转后的值拼接
        如果有无效旋转，flag=FALSE，结束本次循环，
        最后需要满足flag=TRUE并且新的字符串对应的整数不等于原有的整数
        但是此方法做了大量转换和遍历，效率偏低
        """
        dic = {
            '0': '0',
            '1': '1',
            '2': '5',
            '5': '2',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        count = 0
        flag = True
        if N >= 1 and N <= 10000:
            for i in range(1, N + 1):
                s = str(i)
                new_s = ''
                for j in s:
                    if j in dic.keys():
                        rotated_j = dic.get(j)
                        new_s += rotated_j
                        flag = True
                    else:
                        new_s += j
                        flag = False
                        break
                if flag == True and int(new_s) != i:
                    count += 1
            return count


if __name__ == '__main__':
    solution = Solution()
    result = solution.rotatedDigits(int(input()))
    print(result)
