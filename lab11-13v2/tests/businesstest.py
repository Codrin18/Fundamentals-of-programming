'''
Created on Jan 5, 2019

@author: codrin18
'''
import unittest

from domain.business import Plane,Passenger



class PassengerTest(unittest.TestCase):

    def test_create_passenger(self):

        first_name = "Codrin"

        last_name = "Diac"

        passport_number = 199022356

        passenger = Passenger(first_name,last_name,passport_number)

        self.assertEqual(passenger.first,"Codrin")
        self.assertEqual(passenger.last,"Diac")
        self.assertEqual(passenger.passport,199022356)


class PlaneTest(unittest.TestCase):

    def test_create_plane(self):
        first_name = "Codrin"

        last_name = "Diac"

        passport_number = 199022356

        passenger = Passenger(first_name,last_name,passport_number)

        number = 87987987665

        company = "Wizair"

        destination = "Tokyo"

        nr_seats = 30

        x = []

        x.append(passenger)

        plane = Plane(number,company,nr_seats,destination,x)

        self.assertEqual(plane.number,87987987665)

        self.assertEqual(plane.company,"Wizair")

        self.assertEqual(plane.seats,30)

        self.assertEqual(plane.destination,"Tokyo")


if __name__ == "__main__" :
    unittest.main()