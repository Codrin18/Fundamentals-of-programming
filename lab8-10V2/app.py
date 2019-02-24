'''
Created on Dec 10, 2018

@author: codrin18
'''

from domain.vector import MyVector
from infrastructure.repository import VectorRepository
from application.controller import VectorController
from UI.console import VectorUI

repo = VectorRepository()
ctr = VectorController(repo)
ui = VectorUI(ctr)
ui.run()