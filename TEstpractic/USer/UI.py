'''
Created on Jan 15, 2019

@author: codrin18
'''

from application.control import Controller

class UI(object):
    '''
    classdocs
    '''


    def __init__(self):
        
        self.__user = Controller()
        
    @staticmethod
    def print_menu():
        
        s = "Menu"
        s += "\t1.Add political article\n"
        s += "\t2.Add cultural article\n"
        s += "\t3.sort by function  political article\n"
        s += "\t4.sort by function cultural article\n"
        s += "\t5.Sort by python political article\n"
        s += "\t6.Sort by python  cultural article\n"
        s += "\t7.Get all political articles starting with The\n"
        s += "\t8.Get all cultural articles starting with The\n"
        s += "\t9.Get all political articles"
        s += "t10.Get all cultural articles"
        print(s)
        
    def run(self):
        
        UI.print_menu()
        
        while True :
            
            try :
                
                op = int(input("Choose an option from above: "))
                
                self.__user.add_cultural_ctrl("Concersts", 60)
                self.__user.add_cultural_ctrl("Theathere", 125)
                self.__user.add_cultural_ctrl("Events", 50)
                
                self.__user.add_political_ctrl("Local", 175)
                self.__user.add_political_ctrl("President", 200)
                
                
                
                
                if op == 1 :
                    
                    title = str(input("Enter the title of the political article: "))
                    lenght = int(input("Enter the lenght of the political article: "))
                    
                    self.__user.add_political_ctrl(title, lenght)
                    
                if op == 2 :
                    
                    title = str(input("Enter the title of the cultural article: "))
                    lenght = int(input("Enter the lenght of the cultural article: "))
                    
                    self.__user.add_cultural_ctrl(title, lenght)
                    
                if op == 3 :
                    
                    self.__user.sort_political_ctrl()
                    
                if op == 4 :
                    
                    self.__user.sort_cultural_ctrl()
                
                if op == 5 :
                    
                    self.
        
        