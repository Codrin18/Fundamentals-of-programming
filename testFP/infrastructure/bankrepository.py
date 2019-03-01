'''
Created on Dec 4, 2018

@author: codrin18
'''

class BankAccountsRepository():
  
    def __init__(self):
        self.__blist = []
    def sub_string(self,st,name):
        return name.startswith(st)               
    def maximum_money(self,st):
        mx = 0
        for el in self.__blist :
            if self.sub_string(st,el.get_name()) == True :
                if el.get_money() > mx :
                    mx = el.get_money()
        return mx
    
    def remove_accounts(self,val):
        for i in range(len(self.__blist)-1,-1,-1) :
            if self.__blist[i].get_money() < val :
                del self.__blist[i]
    def get_all(self):
        return self.__blist 
        
        