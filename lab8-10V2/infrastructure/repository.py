'''
Created on Nov 26, 2018

@author: codrin18
'''

from domain.vector import MyVector
import matplotlib.pyplot as plt
import numpy 


class VectorRepository():
    '''
    classdocs
    '''


    def __init__(self):
        self.__mylist = []
    
    def verify_id(self,id) :
        for index in range(len(self.__mylist)) :
            if  self.__mylist[index].get_nameID() == id :
                return index
        return -1
    def addVector(self,vec) :
        if self.verify_id(vec.get_nameID()) != -1 :
            raise ValueError("The vector already exists...")
        else :
            self.__mylist.append(vec)
    def get_all(self):
        return self.__mylist
    def get_size(self):
        return len(self.__mylist)
    def getVector(self,index) :
        if index < 0 or index > len(self.__mylist) :
            raise ValueError("Index out of range...")
        else :
            return self.__mylist[index]
    def update_by_index(self,b,index):
        if index < 0 or index > len(self.__mylist) :
            raise ValueError("Index out of range...")
        else :
            self.__mylist[index].set_nameId(b.get_nameID())
            self.__mylist[index].set_colour(b.get_colour())
            self.__mylist[index].set_type(b.get_type())
            self.__mylist[index].set_vec(b.get_vec())
    def update_by_nameID(self,b):
        index = self.verify_id(b.get_nameID())
        if index == -1 :
            raise ValueError("Vector does not exists...")
        else :
            self.__mylist[index].set_nameId(b.get_nameID())
            self.__mylist[index].set_colour(b.get_colour())
            self.__mylist[index].set_type(b.get_type())
            self.__mylist[index].set_vec(b.get_vec())
    def del_by_index(self,index):
        if index < 0 or index > len(self.__mylist) :
            raise ValueError("Index out of range...")
        else :
            del self.__mylist[index]
    def  delVector(self,id) :
        index = self.verify_id(id)
        if index == -1 :
            raise ValueError("The vector does not exists...")
        else :
            del self.__mylist[index]
    def draw(self):
        for el in self.__mylist :
            v =el.get_colour()
            if el.get_type() == 1 :
                v += 'o'
            if el.get_type() == 2 :
                v += '^'
            if el.get_type() == 3 :
                v += 's'
            if el.get_type() > 3 :
                v += 'D'
            plt.plot(el.get_vec(),v)
        plt.show()
    def get_sum_all_vectors_elements(self):
        su = []
        for i in range(len(self.__mylist)) :
            su.appennd(self.__mylist[i].sum_vector())
        return su
    def get_sum_all_vectors(self):
        s = []
        x = self.__mylist[0].get_vec()[:]
        for i in range(1,len(self.__mylist)) :
            self.__mylist[0].add_vectors(self.__mylist[i])
        s.append(self.__mylist[0].get_vec())
        self.__mylist[0] = x[:]
        return s
    def get_vectors_by_sum_elements(self,sum):
        v = []
        for el in self.__mylist :
            if el.sum_vector() == sum :
                v.append(el)
        return v
    def get_vectors_by_min(self,mn):
        v = []
        for el in self.__mylist :
            if el.minimum_vector() < mn :
                v.append(el)
        return v
    def get_sum_by_colour(self,col):
        v = []
        for el in self.__mylist :
            if el.get_colour() == col :
                v.append(el.sum_vector())
        return v
    def get_max_list_by_sum(self,val):
        v = []
        for el in self.__mylist :
            if el.sum_vector() > val :
                v.append(el.maximum_vector())
        return v
    def get_min_vectors(self):
        v = []
        for el in self.__mylist :
            v.append(el.minimum_vector())
        return v
    def get_list_multiplication(self):
        v = []
        for index in range(len(self.__mylist)-1) :
            v.append(self.__mylist[index].multiplication_vectors(self.__mylist[index + 1]))
        return v
    def delete_all(self):
        self.__mylist.clear()
    def delete_by_product(self,val):
        for i in range(len(self.__mylist)-1,-1,-1) :
            if self.__mylist[i].product_vector() > val :
                del self.__mylist[i]
    def delete_between_index(self,index1,index2):
        if index1 > index2 :
            index1,index2 = index2,index1
        for i in range(index2,index1-1,-1) :
            del self.__mylist[i]
    def delete_by_max(self,val):
        for i in range(len(self.__mylist)-1,-1,-1) :
            if self.__mylist[i].maximum_vector() == val :
                del self.__mylist[i]
    def update_scalar(self,sca):
        for el in self.__mylist :
            el.scalar_operation(sca)
    def delete_by_colour(self,col):
        for i in range(len(self.__mylist)-1,-1,-1) :
            if self.__mylist[i].get_colour() == col :
                del self.__mylist[i]


