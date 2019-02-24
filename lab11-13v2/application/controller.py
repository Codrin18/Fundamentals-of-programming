'''
Created on Jan 5, 2019

@author: codrin18
'''

from infrastructure.repository import PlaneRepository,PassengerRepository

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self,plane_repo,passenger_repo):
        
        plane_repo = PlaneRepository()
        passenger_repo = PassengerRepository()
        self.__plane_ctrl = plane_repo
        self.__passenger_ctrl = passenger_repo
        
    def plane_add_ctrl(self,number,company,nr_seats,destination,passengers):
        self.__plane_ctrl.add_plane(number,company,nr_seats,destination,passengers)
        
    def plane_get_by_index_ctrl(self,index):
        self.__plane_ctrl.get_by_index(index)
        
    def plane_get_all_ctrl(self):
        self.__plane_ctrl.planes
        
    def plane_update_by_index_ctrl(self,index, number, company, nr_seats, destination, passengers):
        self.__plane_ctrl.update_by_index(index, number, company, nr_seats, destination, passengers)
    
    def plane_update_by_number_ctrl(self, number, company, nr_seats, destination, passengers):
        self.__plane_ctrl.update_by_number(number, company, nr_seats, destination, passengers)
    
    def plane_delete_by_index_ctrl(self,index):
        self.__plane_ctrl.delete_by_index(index)
    
    def plane_delete_all_ctrl(self):
        self.__plane_ctrl.delete_all()
    
    def plane_delete_between_indexes_ctrl(self,index1,index2):
        self.__plane_ctrl.deleet_between_indexes(index1, index2)
    
    def plane_sort_passengers_last_name_ctrl(self,plane):
        self.__plane_ctrl.sort_passengers_last_name(plane)
    
    def plane_sort_by_nr_passengers_ctrl(self):
        self.__plane_ctrl.sort_planes_by_number_of_passengers()
    
    def plane_sort_planes_by_nr_startswith_ctrl(self,substring):
        self.__plane_ctrl.sort_planes_by_nr_of_passengers_first_name_starting_with(substring)
    
    def plane_sort_by_destination_ctrl(self):
        self.__plane_ctrl.sort_planes_by_destination_and_passengers()
    
    def plane_find_by_weird_pass_ctrl(self):
        self.__plane_ctrl.find_planes_with_passengers_with_passports()
    
    def plane_find_by_nr_startwith_ctrl(self,plane,substring):
        self.__plane_ctrl.find_passenger_from_plane(plane, substring)
    
    def plane_make_groups(self,k):
        self.__plane_ctrl.grup_planes(k)
    
    def plane_make_groups_of_passengers(self,plane,group_size):
        self.__plane_ctrl.group_passengers(group_size, plane)
    
    def passenger_add_ctrl(self,first_name,last_name,passport_number):
        self.__passenger_ctrl.add_passenger(first_name, last_name, passport_number)
    
    def passenger_get_by_index_ctrl(self,index):
        self.__passenger_ctrl.get_by_index(index)
    
    def passenger_get_all_ctrl(self):
        self.__passenger_ctrl.passengersrepo
    
    def passenger_update_by_index_ctrl(self,index,first_name,last_name,passport_number):
        self.__passenger_ctrl.update_by_index(index, first_name, last_name, passport_number)
    
    def passenger_delete_all_ctrl(self):
        self.__passenger_ctrl.delete_all()
    
    def passenger_delete_by_index_ctrl(self,index):
        self.__passenger_ctrl.delete_by_index(index)
    
    def passenger_delete_between_indexes(self,index1,index2):
        self.__passenger_ctrl.delete_between_indexes(index1, index2)
        
    
        
        
        
        
        
        
        
        
        
    