'''
Created on Jan 5, 2019

@author: codrin18
'''

from UI.console import UI

from application.controller import Controller

from infrastructure.repository import PlaneRepository,PassengerRepository

plane_repo = PlaneRepository()

pass_repo = PassengerRepository()

ctrl = Controller(plane_repo,pass_repo)

ui = UI(ctrl)

ui.run()