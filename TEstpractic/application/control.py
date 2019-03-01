'''
Created on Jan 15, 2019

@author: codrin18
'''

from repository.repo import ArticleRepository

class Controller():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__controller = ArticleRepository()
        
    def get_all_political_ctrl(self):
        self.__controller.get_all_political()
        
    def get_all_cultural_ctrl(self):
        self.__controller.get_all_cultural()
        
    def add_political_ctrl(self,title,lenght):
        
        self.__controller.add_new_political(title, lenght)
        
    def add_cultural_ctrl(self,title,lenght):
        
        self.__Controller.add_new_cultural(title,lenght)
        
    def get_all_cultural_start_with_ctrl(self):
        
        self.__controller.get_all_cultural_start_with()
        
    def get_all_political_start_with_ctrl(self):
        
        self.__controller.get_all_political_start_with()
        
    def sort_political_ctrl(self):
        
        self.__controller.sort_political()
        
    def sort_political_by_python_ctrl(self):
        
        self.__controller.sort_political_by_python()
        
    def sort_cultural_ctrl(self):
        
        self.__controller.sort_cultural()
        
    def sort_cultural_by_python(self):
        
        self.__controller.sort_cultural_by_python()
        
        