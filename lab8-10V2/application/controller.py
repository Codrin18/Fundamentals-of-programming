'''
Created on Dec 10, 2018

@author: codrin18
'''

from domain.vector import MyVector
from infrastructure.repository import VectorRepository

class VectorController():
    '''
    classdocs
    '''


    def __init__(self, repo):
        self.__repo = repo
    def add_vector(self,v):
        self.__repo.addVector(v)
    def create_vector(self,nameId,col,t,values):
        vec = MyVector(nameId,col,t,values)
        self.__repo.addVector(vec)
    def getAll(self):
        return self.__repo.get_all()
    def getIndex(self,index):
        return self.__repo.get_by_index(index)
    def updateIndex(self,v,index):
        self.__repo.update_by_index(v,index)
    def updateNameId(self,v):
        self.__repo.update_by_nameID(v)
    def delIndex(self,index):
        self.__repo.del_by_index(index)
    def del_vector(self,id):
        self.__repo.delVector(id)
    def drawc(self):
        self.__repo.draw()
    def sum_all_vector_elements(self):
        return self.__repo.get_sum_all_elements()
    def sum_all_vectors(self):
        return self.__repo.get_sum_all_vectors()
    def get_vector_by_sum(self,sum):
        return self.__repo.get_vectors_by_sum_elements(sum)
    def get_by_min(self,mn):
        return self.__repo.get_vectors_by_min()
    def sum_by_colour(self,col):
        return self.__repo.get_sum_by_colour(col)
    def max_list_by_sum(self,sum):
        return self.__repo.get_max_list_by_sum(sum)
    def min_vectors(self):
        return self.__repo.get_min_vectors()
    def list_multiplication(self):
        return self.__repo.get_list_multiplication()
    def deleteAll(self):
        self.__repo.delete_all()
    def delete_product(self,val):
        self.__repo.delete_by_product(val)
    def between_index(self,index1,index2):
        self.__repo.delete_between_index(index1,index2)
    def delete_max(self,val):
        self.__repo.delete_by_max(val)
    def scalar(self,sca):
        self.__repo.update_scalar()
    def delColour(self,col):
        self.__repo.delete_by_colour(col)