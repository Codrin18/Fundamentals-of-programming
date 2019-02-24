'''
Created on Dec 10, 2018

@author: codrin18
'''

import unittest
from domain.vector import MyVector
from infrastructure.repository import VectorRepository


class VectorRepositoryTest(unittest.TestCase):
    
    def test_addVector(self):
        a = MyVector(1,'r',1,[1,2,3])
        repo = VectorRepository()
        repo.addVector(a)
        self.assertEqual(repo.get_size(),1)
        try :
            b =MyVector(1,'b',1,[4,5,6])
            repo.addVector(b)
        except:
            True
    def test_get_vector(self):
        a = MyVector(1,'r',1,[1,2,3])
        repo = VectorRepository()
        repo.addVector(a)
        try :
            index = 3
            repo.getVector(index)
        except :
            True
        self.assertIs(repo.getVector(0),a)
    def test_update_by_index(self):
        a = MyVector(1,'r',1,[1,2,3])
        repo = VectorRepository()
        repo.addVector(a)
        index = 0
        b =MyVector(1,'r',1,[4,5,6])
        repo.update_by_index(b, index)
    def test_update_by_id(self):
        a = MyVector(1,'r',1,[1,2,3])
        repo = VectorRepository()
        repo.addVector(a)
        b =MyVector(1,'r',1,[4,5,6])
        repo.update_by_nameID(b)
    def test_del_by_index(self):
        a = MyVector(1,'r',1,[1,2,3])
        repo = VectorRepository()
        repo.addVector(a)
        index = 0
        repo.del_by_index(index)
        self.assertEqual(repo.get_size(),0)
    def test_del_by_id(self):
        a = MyVector(1,'r',1,[1,2,3])
        repo = VectorRepository()
        repo.addVector(a)
        id = 1
        repo.delVector(id)
        self.assertEqual(repo.get_size(),0)
    def test_sum_vector(self):
        a = MyVector(1,'r',1,[1,2,3])
        repo = VectorRepository()
        repo.addVector(a)
        self.assertTrue(repo.get_sum_all_vectors())
    
        







if __name__ == "__main__" :
    unittest.main()