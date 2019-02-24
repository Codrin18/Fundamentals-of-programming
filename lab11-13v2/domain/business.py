'''
Created on Jan 5, 2019

@author: codrin18
'''

class Plane():

    def __init__(self,number,company,nr_seats,destination,passengers):

        self.__number = number
        self.__company = company
        self.__seats = nr_seats
        self.__destination = destination
        self.__passengers = passengers[:]

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self,new_number):
        self.__number = new_number

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self,new_company):
        self.__company= new_company

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self,new_nr_seats):
        self__seats = new_nr_seats

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self,new_destination):
        self.__destination =new_destination

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self,new_passenegrs):
        self.__passengers = new_passenegrs[:]

    def __str__(self):

        return (
            f"( {self.__number}, "
            f"{self.__company}, "
            f"{self.__seats}, "
            f"{self.__destination}, "
            f"{self.__passengers}, )"
        )

class Passenger():

    def __init__(self,first_name,last_name,passport_number):

        self.__first = first_name
        self.__last = last_name
        self.__passport = passport_number

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self,first_name):
        self.__fisrt = first_name

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self,last_name):
        self.__last = last_name

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self,passport_number):
        self.__passport = passport_number

    def __str__(self):

        return f"({self.__first}, {self.__last}, {self.__passport})"
