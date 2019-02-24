'''
Created on Nov 1, 2018

@author: codrin18
'''

import logic



def print_menu():
    s = "Menu\n"
    s += "\t 1.Add\n"
    s += "\t 2.Insert\n"
    s += "\t 3.Remove\n"
    s += "\t 4.Remove in range\n"
    s += "\t 5.Replace in range\n"
    s += "\t 6.Prime in range\n"
    s += "\t 7.Odd in range\n"
    s += "\t 8.Sum in range\n"
    s += "\t 9.Greatest common divizor in range\n"
    s += "\t 10.Max in range\n"
    s += "\t 11.Filter prime\n"
    s += "\t 12.Filter negative\n"
    s += "\t 13.Undo the last operation\n"
    s += "\t 0.Exit"
    print(s)

def run():
    
    my_list = []
    prev_list1 = []
    prev_list2 = []
    n = 1
    while n != 0 :
        n = int(input("Select an option please :"))
        prev_list1 = my_list[:]
        if n == 1 :
            add_sub_menu(my_list)
        elif n == 2 :
            insert_sub_menu(my_list) 
        elif n == 3 :
            remove_sub_menu(my_list)
        elif n == 4 :
            remove_in_range_sub_menu(my_list)
        elif n == 5 :
            replace_in_range_sub_menu(my_list)
        elif n == 6 :
            prime_sub_menu(my_list)
        elif n == 7 :
            odd_sub_menu(my_list)
        elif n == 8 :
            sum_sub_menu(my_list)
        elif n == 9 :
            gcd_sub_menu(my_list)
        elif n == 10 :
            max_sub_menu(my_list)
        elif n == 11 :
            filter_prime_sub_menu(my_list)
        elif n == 12 :
            negative_sub_menu(my_list)
        elif n == 13 :
            my_list = prev_list2[:]
            print(my_list)
        elif n == 14 :
            my_list = logic.read_from_files(my_list)
            print(my_list)
        elif n == 15 :
            logic.write_to_file(my_list)             
        if prev_list1 != my_list:
            prev_list2 = prev_list1[:]
            prev_list1 = my_list[:]
        
        

def add_sub_menu(v):
    n = int(input("Enter athe number you want to add :"))
    print(logic.add(v, n))
def insert_sub_menu(v):
    n =int(input("Enter the number you want to insert :"))
    index = int(input("Enter the position please :"))
    v = logic.insertElement(v, index, n)
    print(v)
def remove_sub_menu(v):
    nr = int(input("Enter the number you want to remove :"))
    v = logic.remove_element(v,nr)
    print(v)
def remove_in_range_sub_menu(v):
    start = int(input("Enter a number for start please :"))
    end = int(input("Enter a number for end please :"))
    v = logic.remove_from_start_end(v, start, end)
    print(v)
def replace_in_range_sub_menu(v):
    s1 = []
    s2 = []
    n = int(input("enter an integer : "))
    m = int(input("enter an integer : "))
    for i in range(0, n):
        nr1 = int(input())
        s1.append(nr1)
    for j in range(0, m):
        nr2 = int(input())
        s2.append(nr2)
    v=logic.replace_sublist(v, s1, s2)
    print(v)
    

def prime_sub_menu(v):
    start = int(input("enter a number for start please :"))
    end = int(input("Enter a number for end please "))
    x = logic.print_prime(v, start, end)
    print(x)
def odd_sub_menu(v):
    start = int(input("enter a number for start please :"))
    end = int(input("Enter a number for end please "))
    x = logic.print_prime(v, start, end)
    print(x)
def sum_sub_menu(v):
    start = int(input("enter a number for start please :"))
    end = int(input("Enter a number for end please "))
    x = logic.get_sum_range(v, start, end)
    print(x)
def max_sub_menu(v):
    start = int(input("enter a number for start please :"))
    end = int(input("Enter a number for end please "))
    x = logic.get_max_range(v, start, end)
    print(x)
def gcd_sub_menu(v):
    start = int(input("enter a number for start please :"))
    end = int(input("Enter a number for end please "))
    x = logic.get_gcd_range(v, start, end)
    print(x)
def filter_prime_sub_menu(v):
    v = logic.filter_primes(v)
    print(v)
def negative_sub_menu(v):
    v = logic.filter_negative_numbers(v)
    print(v)



print_menu()
run()     