'''
Created on Jan 5, 2019

@author: codrin18
'''
import unittest
from domain.business import Plane,Passenger
from infrastructure.repository import PlaneRepository,PassengerRepository

class PlaneRepositoryTest(unittest.TestCase):

    def test_add_plane(self):

        repo = PlaneRepository()

        number = 676765775

        company = "Wizair"

        nr_seats = 30

        destination = "Tokyo"

        passenger = PassengerRepository()

        passenger.add_passenger("Codrin","Diac",14567)

        repo.add_plane(number,company,nr_seats,destination,passenger)

        self.assertEqual(repo.get_size(),1)

    def test_update_by_index(self):

        index  = 0

        repo = PlaneRepository()

        number = 676765775

        company = "Wizair"

        nr_seats = 30

        destination = "Tokyo"

        passenger = PassengerRepository()

        passenger.add_passenger("Codrin","Diac",14567)

        repo.add_plane(number,company,nr_seats,destination,passenger)

        repo.update_by_index(index,199,"Wiz",15,"Kyoto",passenger)

        self.assertEqual(repo[index].number,199)

        self.assertEqual(repo[index].company,"Wiz")

        self.assertEqual(repo[index].seats,15)

        self.assertEqual(repo[index].destination,"Kyoto")


    def test_delete_by_index(self):

        index  = 0

        repo = PlaneRepository()

        number = 676765775

        company = "Wizair"

        nr_seats = 30

        destination = "Tokyo"

        passenger = PassengerRepository()

        passenger.add_passenger("Codrin","Diac",14567)

        repo.add_plane(number,company,nr_seats,destination,passenger)

        repo.delete_by_index(index)

        self.assertEqual(repo.get_size(),0)

        




if __name__ == "__main__":
    unittest.main()