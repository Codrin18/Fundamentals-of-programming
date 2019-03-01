'''
Created on Dec 4, 2018

@author: codrin18
'''

import unittest
from infrastructure.bankrepository import BankAccountsRepository
from domain.bank import BankAccounts

class MyClass(unittest.TestCase):
    
    def test_bank_repo(self):
        a = BankAccountsRepository()
        b1 = BankAccounts("Codrin",1100)
        b2 = BankAccounts("Eugen",1200)
        a.append(b1)
        a.ppend(b2)
        a.remove_accounts(1200)
        self.assertEqual(a.get_all(),[("Eugen",1200)])
        