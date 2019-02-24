'''
Created on Dec 10, 2018

@author: codrin18
'''

from application.controller import VectorController
from domain.vector import MyVector

class VectorUI():
    '''
    classdocs
    '''


    def __init__(self, controller):
        self.__controller = controller
    
    
    @staticmethod
    def print_menu():
        s = "Menu\n"
        s +="\t0.Exit\n"
        s +="\t1.Add a vector to the repository\n "
        s +="\t2.Get all vectors\n"
        s +="\t3.Get a vector at a given index\n"
        s +="\t4.Update a vector at a given index\n"
        s +="\t5.Update a vector identified by name_id\n"
        s +="\t6.Delete a vector by index\n"
        s +="\t7.Delete a vector by name_id\n"
        s +="\t8.Plot all vectors in\n"
        s +="\t9.Sum of all elements\n"
        s +="\t10.Sum of all vectors"
        s +="\t11.List of vectors having a given sum of elements\n"
        s +="\t12.Vectors having minimum less than a given value\n"
        s +="\t13.Sum of all elements by colour\n"
        s +="\t14.Get the max of all vectors having the sum greater than a given value\n"
        s +="\t15.Get the min of all vectors\n"
        s +="\t16.Multiplication of consecutive vectors\n"
        s +="\t17.Delete all vectors from the repository\n"
        s +="\t18.Delete all vectors for which the colour is a given value\n"
        s +="\t19.Delete all vectors for which the product of elements is greater than a given value"
        s +="\t20.Delete all vectors that are between two given indexes\n"
        s +="\t21.Delete all vectors for which the max value is equal to a given value|n"
        s +="\t22.Update all vectors by adding a given scalar to each element\n"
        s +="\t23.Update the colour of a vector identified by name_id\n"
        s +="\t24.Update all vectors having a given type by setting their colour to the same given value\n"
        print(s)
    def run(self):
        while True :
            try :
                n = int(input("enter an option : "))
                if n == 0 :
                    break
                if n == 1 :
                    nameId = int(input("enter an id : "))
                    col = str(input("enter a colour: "))
                    t = int(input("enter a type: "))
                    len_vals = int(input('How many values do you want to add? '))

                    values = []
                    for _ in range(len_vals):
                        values.append(int(input('Enter new value: ')))
                    self.__controller.create_vector(nameId,col,t,values)
                if n == 2 :
                    self.__controller.get_all()
                if n == 3 :
                    index = int(input("enter an index : "))
                    self.__controller.getIndex(index)
                if n == 4 :
                    index = int(input("enter an index : "))
                    self.__controller.updateIndex(index)
                if n == 5 :
                    nameId = int(input("enter an id : "))
                    col = str(input("enter a colour: "))
                    t = int(input("enter a type: "))
                    len_vals = int(input('How many values do you want to add? '))

                    values = []
                    for _ in range(len_vals):
                        values.append(int(input('Enter new value: ')))
                    v = MyVector(nameId,col,t,values)
                    self.__controller.updateNameId(v)
                if n == 6 :
                    index = int(input("Enter an index : "))
                    self.__controller.delIndex(index)
                if n == 7 :
                    nameId = int(input("Enter a nameId : "))
                    self.__controller.del_vector()
                if n == 8 :
                    self.__controller.drawc()
                if n == 9 :
                    self.__controller.sum_all_vector_elements()
                if n == 10 :
                    self.__controller.sum_all_vectors()
                if n == 11 :
                    s = int(input("enter a value : "))
                    x = self.__controller.get_vector_by_sum(s)
                if n == 12 :
                    mn = int(input("Enter a min : "))
                    x = self.__controller.get_by_min(mn)
                if n == 13 :
                    col = str(input("enter a colour: "))
                    x = self.__controller.sum_by_colour(col)
                if n == 14 :
                    s = int(input("Enter an integre value : "))
                    print(self.__controller.max_list_by_sum(s))
                if n == 15 :
                    print(self.__controller.min_vectors())
                if n == 16 :
                    print(self.__controller.multiplication_vectors())
                if n == 17 :
                    self.__controller.deleteAll()
                if n == 18 :
                    col = str(input("enter a colour: "))
                    self.__controller.delColour(col)
                if n == 19 :
                    val = int(input("Enter an integer : "))
                    self.__controller.delete_by_product(val)
                if n == 20 :
                    index1 = int(input("Enter the first index : "))
                    index2 = int(input("Enter the second index : "))
                    self.__controller.between_index(index1,index2)
                if n == 21 :
                    val = int(input("Enter an integer : "))
                    self.__controller.delete_max(val)
                if n == 22 :
                    sca = int(input("enter an integer: "))
                    self.__controller.sca(sca)
            except Exception as e :
                print("An error ocuured " + str(e))
