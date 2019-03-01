'''
Created on Dec 4, 2018

@author: codrin18
'''

from domain.bank import BankAccounts
from infrastructure

class BankAccountsUI():
    
    def __init__(self,repo):
        self.__repo = repo 
    
    @staticmethod
    def prin_menu():
        s = "Menu\n"
        s += "\t1.Maximum Money\n"
        s += "\t2.Remove accounts\n"
        print(s)
    def run(self):
        
        BankAccountsUI.prin_menu()
        while True :
            option = int(input("Enter an option : "))
            if option == 1 :
                st = input()
                self.__repo.maximum_money()
            if option == 2 :
                n = int(input("Enter an integer : "))
                self.__repo.remove_accounts(n)
            if option == 0 :
                break