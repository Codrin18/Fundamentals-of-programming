'''
Created on Nov 26, 2018

@author: codrin18
'''

class MyVector():
    '''
    classdocs
    '''
    def __init__(self,nameId,c,t,values = []) :
        self.__nameId = nameId
        self.__colour = c
        self.__type = t
        self.__vlist = values
        
    def set_nameId(self,name) :
        self.__nameId = name
        
    def get_nameID(self) :
        return self.__nameId
    
    def set_colour(self,c):
        if c in ['r','g','b','y','m'] == False :
            raise Exception("The colour is not good...")
        else :
            self.__colour = c
            
    def get_colour(self):
        return self.__colour
    
    def set_type(self,t):
        self.__type = t
        
    def get_type(self):
        return self.__type
    
    def get_vec(self) :
        return self.__vlist
    
    def set_vec(self,vec) :
        self.__vlist = vec[:]
            
    def scalar_operation(self,sca) :
        if not self.__vlist :
            raise Exception("The vector is empty...")
        else :
            for i in range(len(self.__vlist)) :
                    self.__vlist[i] += sca 
    def add_vectors(self,other):
        if len(self.__vlist) != len(other.__vlist) :
            raise ValueError("The vectors do not have the same length...")
        else :
            for i in range(len(self.__vlist)) :
                self.__vlist[i] = self.__vlist[i] + other.__vlist[i]
                
    def dif_vectors(self,other) :
        if len(self.__vlist) != len(other.__vlist) :
            raise Exception("Vectors are not equal...")
        else :
            for i in range(len(self.__vlist)) :
                self.__vlist[i] = self.__vlist[i] - other.__vlist[i]
                
    def multiplication_vectors(self,other) : 
        if len(self.__vlist) != len(other.__vlist) :
            raise ValueError("The vectors do not have the same length...")
        else :
            m = 0
            for i in range(len(self.__vlist)) :
                m = m + self.__vlist[i] * other.__vlist[i] 
            return m
    def sum_vector(self):  
        if len(self.__vlist) == 0 :
            raise ValueError("The vector does not have elements...")
        else :
            s = 0
            for i in range(len(self.__vlist)) :
                s = s + self.__vlist[i]
            return s
    
    def product_vector(self):
        if len(self.__vlist) == 0 :
            raise ValueError("The vector does not have elements...")
        else :
            p = 1
            for i in range(len(self.__vlist)) :
                p = p * self.__vlist[i]
            return p
        
    def average_vector(self) :
        if len(self.__vlist) == 0 :
            raise ValueError("The vector is empty...")
        else :
            s = 0
            for i in range(len(self.__vlist)) :
                s = s + self.__vlist[i]
        return s//len(self.__vlist)  
    
    def minimum_vector(self):
        if len(self.__vlist) == 0 :
            raise ValueError("The vector does not have elements...")
        else :
            mn = self.__vlist[0]
            for i in range(len(self.__vlist)) :
                if mn > self.__vlist[i] :
                    mn = self.__vlist[i]
            return mn
    def maximum_vector(self):
        if len(self.__vlist) == 0 :
            raise ValueError("The vector does not have elements...")
        else :
            mx = self.__vlist[0]
            for i in range(len(self.__vlist)) :
                if mx < self.__vlist[i] :
                    mx = self.__vlist[i]
            return mx