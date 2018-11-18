"""
一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。

给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。
"""


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        """
        很直接的思路，使用一个哈希表存储域名和其对应的出现次数。
        添加到哈希表的时候，键不存在，则直接将count值赋值为value；键已经存在，则将count与value相加
        剩下的就是字符串分隔拼接的操作
        """
        dic = {}
        res = []
        for i in cpdomains:
            list = i.split(' ')
            count = int(list[0])
            domain_list = list[1].split('.')
            for j in range(len(domain_list)):
                domain = '.'.join(domain_list[j::])
                if domain in dic.keys():
                    dic[domain] = dic.get(domain) + count
                else:
                    dic[domain] = count
        for i in dic.keys():
            res.append(str(dic.get(i)) + ' ' + i)
        return res


if __name__ == '__main__':
    input_list = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    solution = Solution()
    result = solution.subdomainVisits(input_list)
    print(result)
