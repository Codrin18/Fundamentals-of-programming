'''
Created on Dec 4, 2018

@author: codrin18
'''

class BankAccounts():
    '''
    classdocs
    '''
    def __init__(self,name,nr):
        self.__name = name
        self.__money = nr
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_money(self):
        return self.__money
    def set_money(self,nr):
        self.__money = nr
        