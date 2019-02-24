'''
Created on Nov 13, 2018

@author: codrin18
'''
from Domain.Repository import PointRepository
from Domain.MyPoint import MyPoint

def test_add():
    repo = PointRepository()
    s1 = MyPoint(2,3,"green")
    repo.add(s1)
    assert repo.size() == 1

test_add()