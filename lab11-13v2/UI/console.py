'''
Created on Jan 5, 2019

@author: codrin18
'''

from application.controller import Controller
from infrastructure.repository import PassengerRepository,PlaneRepository

class UI(object):
    '''
    classdocs
    '''


    def __init__(self,controller):
        
        repo1 = PlaneRepository()
        repo2 = PassengerRepository()
        controller = Controller(repo1,repo2)
        
        self.__controller = controller
        
    @staticmethod
    def print_menu():
        
        s = "Menu"
        s += "\t 1.Add plane\n"
        s += "\t 2.Get plane by index\n"
        s += "\t 3.Get all planes"
        s += "\t 4.Update plane by index\n"
        s += "\t 5.Update plane by number\n"
        s += "\t 6.Delete plane by index\n "
        s += "\t 7.Delete all planes\n"
        s += "\t 8.Delete plane by number\n"
        s += "\t 9.Delete planes between indexes\n"
        s += "\t 10.Sort passengers in a plane by last name\n"
        s += "\t 11.Sort planes by number of passengers\n"
        s += "\t 12.Sort by number of first name starting with a substring\n"
        s += "\t 13.Sort by concatenation of passenger and destination\n"
        s += "\t 14.Find by weird passport\n"
        s += "\t 15.Find by nr starting with a substring\n"
        s += "\t 16.Make groups of plane\n "
        s += "\t 17.Make groups of passenger in a plane\n"
        s += "\t 18.Add passenger\n"
        s += "\t 19.Get passenger by index\n"
        s += "\t 20.Get all passengers\n"
        s += "\t 21.Delete all passengers\n"
        s += "\t 22.Delete passenger by index\n"
        s += "\t 23.Delete between two indexes passengers\n"
        s += "\t 24.Update by index passenger\n"
        s += "\t 0.Exit\n"
        
        print (s)
        
    def run(self):
        
        UI.print_menu()
        
        try :
            
            while True:
                
                option = int(input("Please choose an option from above: "))
                
                if option == 0 :
                    break
                
                if option == 1 :
                    
                    number = int(input("Enter a number for a plane: "))
                    company = str(input("Enter the company: "))
                    nr_seats = int(input("Enter a number of seats: "))
                    destination = str(input("Enter a destination: "))
                    nr = int(input("How many passengers? "))
                    pass_repo = PassengerRepository()
                    
                    for i in range(nr):
                        first_name = str(input("Enter the first name of the passenger: "))
                        last_name =  str(input("Enter the last name of a passenger: "))
                        passport = int(input("Enter the number of the passport: "))
                        pass_repo.add_passenger(first_name,last_name,passport)
                    
                    self.__controller.plane_add_ctrl(number, company, nr_seats, destination, pass_repo)
                    
                    print("The plane was added...")
                    
                if option == 2 :
                    
                    index = int(input("Enter an index: "))
                    
                    return self.__controller.plane_get_by_index_ctrl(index)
                
                if option == 3 :
                    
                    return self.__controller.plane_get_all_ctrl()
                
                if option == 4 :
                    
                    index = int(input("Enter an index"))
                    number = int(input("Enter a number for a plane: "))
                    company = str(input("Enter the companyu: "))
                    nr_seats = int(input("Enter a number of seats: "))
                    destination = str(input("Enter a destination: "))
                    nr = int(input("How many passengers? "))
                    pass_repo = PassengerRepository()
                    
                    for i in range(nr):
                        first_name = str(input("Enter the first name of the passenger: "))
                        last_name =  str(input("Enter the last name of a passenger: "))
                        passport = int(input("Enter the number of the passport: "))
                        pass_repo.add_passenger(first_name,last_name,passport)
                
                        
                    self.__controller.plane_update_by_index_ctrl(index, number, company, nr_seats, destination, pass_repo)
                    
                if option == 5 :
                    
                    number = int(input("Enter a number for a plane: "))
                    company = str(input("Enter the companyu: "))
                    nr_seats = int(input("Enter a number of seats: "))
                    destination = str(input("Enter a destination: "))
                    nr = int(input("How many passengers? "))
                    pass_repo = PassengerRepository()
                    i = 0
                    while i < nr :
                        first_name = str(input("Enter the first name of the passenger: "))
                        last_name =  str(input("Enter the last name of a passenger: "))
                        passport = int(input("Enter the number of the passport: "))
                        pass_repo.add_passenger(first_name,last_name,passport) 
                        i = i + 1
                        
                    self.__controller.plane_update_by_number_ctrl(number, company, nr_seats, destination, pass_repo)
                    
                if option == 6 :
                    
                    index = int(input("Enter an index: "))
                    
                    self.__controller.plane_delete_by_index_ctrl(index)
                    
                if option == 7 :
                    
                    self.__Controller.plane_delete_all_ctrl()
                    
                if option == 9 :
                    
                    index1 = int(input("Enter an index: "))
                    index2 = int(input("Enter an index: "))
                    self.__controller.plane_delete_between_indexes_ctrl(index1,index2)
                
                if option == 10 :
                    
                    index = int(input("Enetr the index of the plane that will sort their passengers by last name: "))
                    
                    self.__controller.plane_sort_passengers_last_name_ctrl(self.__controller.plane_get_by_index_ctrl(index))
                    
                if option == 11 :
                    
                    self.__controller.plane_sort_by_nr_passengers_ctrl()
                    
                if option == 12 :
                    
                    substring = str(input("Enter a substring: "))
                    
                    self.__controller.plane_sort_planes_by_nr_startswith_ctrl(substring)
                    
                if option == 13 :
                    
                    self.__controller.plane_sort_by_destination_ctrl()
                    
                if option == 14 :
                    
                    self.__controller.plane_find_by_weird_pass_ctrl()
                
                if option == 15 :
                    
                    index = int(input("Enter an index: "))
                    substring = str(input("Enter a substring: "))
                    
                    self.__controller.plane_find_by_nr_startwith_ctrl(self.__controller.plane_get_by_index_ctrl(index),substring)
                    
                if option == 16 :
                    
                    k = int(input("Enter the group size: "))
                    
                    self.__controller.plane_make_groups(k)
                    
                if option == 17 :
                    
                    index = int(input("Enter an index: "))
                    k = int(input("Enter the group size: "))
                    
                    self.__Controller.plane_make_groups_of_passengers(self.__controller.plane_get_by_index_ctrl(index),k)
                
                if option == 18 :
                    
                    first_name = str(input("Enter the first name of the passenger: "))
                    last_name =  str(input("Enter the last name of a passenger: "))
                    passport = int(input("Enter the number of the passport: "))
                    self.__controller.passenger_add_ctrl(first_name, last_name, passport)
                    
                if option == 19 :
                    
                    index = int(input("Enter an index: "))
                    self.__controller.passenger_get_by_index_ctrl(index)
                
                if option == 20 :
                    
                    self.__controller.passenger_get_all_ctrl()
                
                if option == 21 :
                    
                    self.__controller.passenger_delete_all_ctrl()
                    
                if option == 22 :
                    
                    index = int(input("Enter an index: "))
                    self.__controller.passenger_delete_by_index_ctrl(index)
                    
                if option == 23 :
                    
                    index1 = int(input("Enter an index: "))
                    index2 = int(input("Enter an index: "))
                    self.__controller.passenger_delete_between_indexes(index1, index2)
                    
                if option == 24 :
                    
                    index = int(input("Enter an index: "))
                    first_name = str(input("Enter the first name of the passenger: "))
                    last_name =  str(input("Enter the last name of a passenger: "))
                    passport = int(input("Enter the number of the passport: "))
                    self.__controller.passenger_update_by_index_ctrl(index, first_name, last_name, passport)
                    
                    
        except Exception as e :
            print("An error occured" + str(e))  
                
                
        
        
        
        
        
        
        
        
        
        