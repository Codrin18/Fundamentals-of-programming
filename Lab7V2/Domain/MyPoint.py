'''
Created on Nov 13, 2018

@author: codrin18
'''

class MyPoint():
    
    def __init__(self,x,y,col):
        self.__coord_x = x 
        self.__coord_y = y
        self.__colour = col
    def get_x(self):
        return self.__coord_x
    def set_x(self,x):
        self.__coord_x = x
    def get_y(self):
        return self.__coord_y 
    def set_y(self,y):
        self.__coord_y = y
    def get_colour(self):
        return self.__colour
    def set_colour(self,col):
        self.__colour = col
    def __str__(self): 
        s = "Point"
        return s + "(" + str(self.__coord_x) + "," + str(self.__coord_y) + ")" + "of colour " + self.__colour   
        