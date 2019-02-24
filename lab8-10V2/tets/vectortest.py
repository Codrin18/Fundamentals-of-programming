'''
Created on Nov 26, 2018

@author: codrin18
'''

import unittest
from domain.vector import MyVector

class MyVectorTest(unittest.TestCase):
    
    def test_create(self):
        v = MyVector(1,'r',1,[1,2,3])
        self.assertEqual(v.get_nameID(),1)
        self.assertEqual(v.get_colour(),'r')
        self.assertEqual(v.get_type(),1)
        self.assertEqual(v.get_vec(),[1,2,3])
        
        v.set_nameId(2)
        v.set_colour('g')
        v.set_type(2)
        v.set_vec([4,5,6])
        self.assertEqual(v.get_nameID(),2)
        self.assertEqual(v.get_colour(),'g')
        self.assertEqual(v.get_type(),2)
        self.assertEqual(v.get_vec(),[4,5,6])
        try :
            v.set_colour('a')
        except ValueError :
            True
    
    def test_scalar(self):
        v = MyVector(1,'r',1,[1,2,3])
        v.scalar_operation(2)
        self.assertEqual(v.get_vec(),[3,4,5])
    def test_add(self):
        a = MyVector(1,'r',1,[1,2,3])
        b = MyVector(2,'r',1,[1,2,3])
        a.add_vectors(b)
        self.assertEqual(a.get_vec(),[2,4,6])
    def test_dif(self):
        a = MyVector(1,'r',1,[1,2,3])
        b = MyVector(2,'r',1,[1,2,3])
        a.dif_vectors(b)
        self.assertEqual(a.get_vec(),[0,0,0])
    def test_multiplication(self):
        a = MyVector(1,'r',1,[1,2,3])
        b = MyVector(2,'r',1,[4,5,5])
        self.assertEqual(a.multiplication_vectors(b),29)
    def test_sum(self):
        a = MyVector(1,'r',1,[1,2,3])
        self.assertEqual(a.sum_vector(),6)
    def test_product(self):
        a = MyVector(1,'r',1,[1,2,3])
        self.assertEqual(a.product_vector(),6)
    def test_average(self):
        a = MyVector(1,'r',1,[1,2,3])
        self.assertEqual(a.average_vector(),2)
    def test_minimum(self):
        a = MyVector(1,'r',1,[1,2,3])
        self.assertEqual(a.minimum_vector(),1)
    def test_maximum(self):
        a = MyVector(1,'r',1,[1,2,3])
        self.assertEqual(a.maximum_vector(),3)



if __name__ == "__main__" :
    unittest.main()