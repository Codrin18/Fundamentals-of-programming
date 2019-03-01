'''
Created on Jan 15, 2019

@author: codrin18
'''

from domain.business import Article
from infrastructure.utils import (
    sort_by_function,
    sort_by_python
    )


class ArticleRepository():
    '''
    classdocs
    '''


    def __init__(self):
        
        self.__political = []
        
        self.__cultural = []
        
    def get_all_political(self):
        return self.__political
    
    def get_all_cultural(self):
        
        return self.__cultural
    
    def add_new_political(self,title,lenght):
        
        if title == " " or lenght <= 0 :
            raise ValueError("The article has to have a title and lenght...")
        
        self.__political.append(Article(title,lenght))
        
    def add_new_cultural(self,title,lenght):
        
        if title == " " or lenght <= 0 :
            raise ValueError("The article has to have a title and lenght...")
        
        self.__cultural.append(Article(title,lenght))
        
    def get_all_political_start_with(self):
        
        return list(filter(lambda x : x.title().startswith("The")),self.__political)
    
    def get_all_cultural_start_with(self):
        
        return list(filter(lambda x : x.title().startswith("The")),self.__cultural)
    
    def sort_political(self):
        
        return sort_by_function(self.__political,lambda x,y : x.lenght() < y.lenght())
    
    def sort_political_by_python(self):
        
        return sort_by_python(self.__political,lambda x,y : x.lenght() < y.lenght())
    
    def sort_cultural(self):
        
        return sort_by_function(self.__cultural,lambda x,y: x.lenght() < y.lenght())
    
    def sort_cultural_by_python(self):
        
        return sort_by_python(self.__cultural,lambda x,y : x.lenght() < y.lenght())
        
    