'''
Created on Jan 15, 2019

@author: codrin18
'''

class Article():
    '''
    classdocs
    '''


    def __init__(self,title,lenght):
        '''
        Constructor
        '''
        self.__title = title
        self.__lenght = lenght
        
    @property 
    def title(self):
        return self.__title
    
    @title.setter 
    def title(self,new_title):
        
        self.__title = new_title
        
    @property 
    def lenght(self):
        return self.__lenght
    
    @lenght.setter 
    def lenght(self,new_lenght):
        self.__lenght = new_lenght
        
    def __str__(self):
        
        s = "The article has the title " + self.__title + "and a lenght " + str(self.__lenght)
        return s
        