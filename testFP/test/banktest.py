'''
Created on Dec 4, 2018

@author: codrin18
'''
import unittest
from domain.bank import BankAccounts

class BankAccountsTest(unittest.TestCase):
    
    def test_bank(self):
        b = BankAccounts("Codrin",1200)
        self.assertEqual(b.get_name(),"Codrin")
        self.assertEqual(b.get_money(),1200)
        
        b.set_name("Eugen")
        self.assertEqual(b.get_name(),"Eugen")
        b.set_money(1100)
        self.assertEqual(b.get_money(),1100)
        