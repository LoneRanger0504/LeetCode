# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。

比如，员工1是员工2的领导，员工2是员工3的领导。他们相应的重要度为15, 10, 5。那么员工1的数据结构是[1, 15, [2]]，员工2的数据结构是[2, 10, [3]]，员工3的数据结构是[3, 5, []]。注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，因此没有体现在员工1的数据结构中。

现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。

"""


# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        """
        深度优先遍历即可，需要另外写一个根据Id获取employee对象的函数
        每次取出一个员工对象，累加重要度，再根据下属列表的id获取下属员工对象加到队列
        """
        if not employees:
            return 0

        def get_employee(eid):
            for employee in employees:
                if employee.id == eid:
                    return employee

        queue = []
        res = 0
        queue.append(get_employee(id))
        while queue:
            employee = queue.pop(0)
            res += employee.importance
            for subordinate in employee.subordinates:
                queue.append(get_employee(subordinate))
        return res


if __name__ == '__main__':
    #  这里的员工对象不好创建，但是代码都是可以ac的
    pass
