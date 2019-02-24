'''
Created on Jan 5, 2019

@author: codrin18
'''


from domain.business import Plane,Passenger

from infrastructure.utils import (
sort_by_function,
search_by_function,
filter_by_function,
my_backtracking
)

class PlaneRepository():

    def __init__(self):

        self.__planes = []

    @property
    def planes(self):
        return self.__planes

    @planes.setter
    def planes(self,planes):
        self.__planes = planes

    def get_size(self):
        return len(self.__planes)


    def add_plane(self,number,company,nr_seats,destination,passengers):
        
        index = self.get_index_by_number(number)
        if index > 0 :
            raise ValueError("Plane already exists...")

        self.__planes.append(Plane(number,company,nr_seats,destination,passengers))


    def get_index_by_number(self,number):

        for index in range(len(self.__planes)) :
            if self.__planes[index].number == number :
                return index

        return -1

    def get_by_index(self,index):

        if index < 0 or index >= len(self.__planes) :
            raise ValueError("Index out of range...")

        return self.__planes[index]

    @staticmethod
    def update_plane(plane,number,company,nr_seats,destination,passengers):
        plane.number = number
        plane.company= company
        plane.seats = nr_seats
        plane.destination = destination
        plane.passengers = passengers

    def update_by_index(self,index,number,company,nr_seats,destination,passengers) :

        if index <0 or index >= len(self.__planes) :
            raise ValueError("Index out of range...")

        self.update_plane(self.__planes[index],number,company,nr_seats,destination,passengers)

    def update_by_number(self,number,company,nr_seats,destination,passengers) :

        index = self.get_index_by_number(number)
        if index < 0 :
            raise ValueError("The plane does not exist...")

        self.update_plane(self.__planes[index],number,company,nr_seats,destination,passengers)

    def delete_by_index(self,index):

        if index < 0 or index >= len(self.__planes) :
            raise ValueError("Index out of range...")

        del self.__planes[index]

    def delete_by_number(self,number):

        index = self.get_index_by_number(number)
        if index < 0 :
            raise ValueError("The plane does not exist...")

        del self.__planes[index]

    def delete_all(self) :

        self.__planes.clear()

    def deleet_between_indexes(self,index1,index2) :

        if index1 > index2 :
            index1,index2 = index2,index1

        for i in range(index2,index1-1,-1):
            del self.__planes[i]

    def sort_passengers_last_name(self,plane):

        plane.passengers = sort_by_function(plane.passengers,lambda x,y: x.last <= y.last)

    def sort_planes_by_number_of_passengers(self):

        self.__planes = sort_by_function(self.__planes, lambda x,y: len(x.passengers) <= len(y.passengers))

    def sort_planes_by_nr_of_passengers_first_name_starting_with(self,substring):

        def get_nr(plane,substring):

            nr = 0
            for el in plane:
                if el.first.startswith(substring) is True :
                    nr = nr + 1

            return nr

        return sort_by_function(self.__planes,lambda x,y: get_nr(x) <= get_nr(y))


    def sort_planes_by_destination_and_passengers(self):

        def concatenation(plane):
            return str(len(plane.passengers)) + plane.destination

        return sort_by_function(self.__planes, lambda x,y: concatenation(x) <= concatenation(y))

    def find_planes_with_passengers_with_passports(self):

        def condition(plane):

            return any(
                [
                    p.passport[0] == p.passport[1] and p.passport[1] == p.passport[2] for p in plane.passengers
                ]
            )

        return filter_by_function(self.__planes,condition)

    def find_passenger_from_plane(self,plane,substring):

        return filter_by_function(plane.passengers,lambda x: substring in x.first or substring in x.last)


    def construct_solution(self,sol,my_list):

        res = []

        for i in sol :
            res.append(my_list[i])

        return res

    def group_passengers(self,group_size,plane):

        def c1(sol,my_list):

            for  i in range(len(sol)-1):
                if  my_list[sol[i]].last == my_list[sol[-1]].last :
                    return False

            return True


        my_list = plane.passengers

        param = [group_size]

        constraints = [c1]

        aux = []

        for el in my_backtracking(param,my_list,constraints):
            aux.append(self.construct_solution(el,my_list))

        if aux == [] :
            return "This plane does not have valid passengers for gruping"

        return aux

    def grup_planes(self,group_size):

        def c1(sol,my_list):

            for i in range(len(sol)-1):
                if my_list[sol[i]].destination != my_list[sol[-1]].destination :
                    return False

            return True

        def c2(sol,my_list):

            for i in range(len(sol)-1):
                if my_list[sol[i]].company == my_list[sol[-1]].company :
                    return False

            return True

        my_list = self.__plane[:]

        param = [group_size]

        constraints = [c1,c2]

        aux = []

        for el in my_backtracking(param,my_list,constraints):
            aux.append(self.construct_solution(el,my_list))

        if aux == [] :
            return "This repository does not have valid planes for gruoping"

        return aux


class PassengerRepository():

    def __init__(self):

        self.__passengersrepo = []

    @property
    def passengersrepo(self):
        return self.__passengersrepo

    @passengersrepo.setter
    def passengersrepo(self,passengersrepo):
        self.__passengersrepo = passengersrepo

    def add_passenger(self,first_name,last_name,passport_number):
        
        index = self.get_index_by_passport(passport_number)
        if index > 0 :
            raise ValueError("Passenger already exists...")

        self.__passengersrepo.append(Passenger(first_name,last_name,passport_number))


    def get_index_by_passport(self,passport):

        for index in range(len(self.__passengersrepo)):
            if self.__passengersrepo[index].passport == passport :
                return index

        return -1


    def get_by_index(self,index):

        if index < 0 or index >= len(self.__passengersrepo):
            raise ValueError("Index out of range...")

        return self.__passengersrepo[index]


    @staticmethod
    def update_passenger(passenger,first_name,last_name,passport_number):
        passenger.first = first_name
        passenger.last = last_name
        passenger.passport = passport_number

    def update_by_index(self,index,first_name,last_name,passport_number):

        if index < 0 or index >= len(self.__passengersrepo):
            raise ValueError("Index out of range...")

        self.update_passenger(self.__passengersrepo[index],first_name,last_name,passport_number)

    def delete_by_index(self,index):

        if index < 0 or index >= len(self.__passengersrepo):
            raise ValueError("Index out of range...")

        del self.__passengersrepo[index]

    def delete_all(self):
        self.__passengersrepo.clear()

    def delete_between_indexes(self,index1,index2):

        if index1 > index2 :
            index1,index2 =index2,index1

        for i in range(index2,index1-1,-1):
            del self.__passengersrepo[i]
            
            

    
