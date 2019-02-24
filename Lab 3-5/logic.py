'''
Created on Nov 1, 2018

@author: codrin18
'''

import math
from Crypto.Util.number import isPrime

def tets_add() : #test function for add
    v = []
    add(v,1)
    assert v[len(v)-1] == 1
    v = []
    add(v,2)
    assert v[len(v)-1] == 2
    v = []
    add(v,3)
    assert v[len(v)-1] == 3
    v = []
    add(v,4)
    assert v[len(v)-1] == 4
    v = []
    add(v,5)
    assert v[len(v)-1] == 5
def add(v,n) :
    '''
Description : Adds a number on the last position of a list
Data : v,n
Precondition : V - a list
               n - interger number
'''
    v.append(n)
    return v

tets_add()

def test_insert() : #test function for insertElement
    v = [1,2]
    insertElement(v,1,2)
    assert v[1] == 2
    v = [1,3,4,5]
    insertElement(v,1,2)
    assert v[1] == 2
    v = [1]
    insertElement(v,0,2)
    assert v[0] == 2
    v = [1,11]
    insertElement(v,1,0)
    assert v[1] == 0
    v = [0,0,0]
    insertElement(v,0,1)
    assert v[0] == 1
def insertElement(v,index,nr) :
    '''
Description : Inserts an elemnt on the position index
Data : v,index,nr
Precondition : v- lits
               index-natural number
               nr - integer 
'''
    v.insert(index,nr)
    return v

test_insert()

def test_remove_element() : #test function for remove
    assert remove_element([1,2,3],1) == [1,3]
    assert remove_element([11,22,3,4,5],0) == [22,3,4,5]
    assert remove_element([5,3,2,1],3) ==[5,3,2]
    assert remove_element([1,2,9,10,11,14,15,16,17],3) == [1,2,9,11,14,15,16,17]
    assert remove_element([1,2,3],2) == [1,2]
def remove_element(v,index) :
    '''
Description : Removes the elemnt situated on the position index
Data : v,index
Precondition : v-list
               index-natural number
'''
    del v[index]
    return v

test_remove_element()

def test_remove_from_start_end() : #test function for remove_from_start_end
    assert remove_from_start_end([1,2,3,4,5,6,7,8,9,10],1,3) == [1,4,5,6,7,8,9,10]
    assert remove_from_start_end([1,2,3,4,5,6,7,8,9,10],1,2) == [1,3,4,5,6,7,8,9,10]
    assert remove_from_start_end([1,2,3,4,5,6,7,8,9,10],7,9) == [1,2,3,4,5,6,7,10]
    assert remove_from_start_end([1,2,3,4,5,6,7,8,9,10],4,6) == [1,2,3,4,7,8,9,10]
    assert remove_from_start_end([1,2,3,4,5,6,7,8,9,10],2,3) == [1,2,4,5,6,7,8,9,10] 
'''
Description : Removes elements from a list starting from the position start until position end
Data : v,start,end
Precondition : v-list,start and end natural numbers,start<end
'''
def remove_from_start_end(v,start,end) :
    '''
Description : Removes elements from a list starting from the position start until position end
Data : v,start,end
Precondition : v-list,start and end natural numbers,start<end
'''
    del v[start:end]
    return v

test_remove_from_start_end()

def find_first_sublist(my_list,sublist,start = 0):
    '''
    Description : It find the first aparition of a sublist
    Data : my_list,sub_list,start
    Precondition : my_list,sub_list - lists ; start -natural number
    Result :The first appearence
    '''
    length = len(sublist)
    for index in range(start, len(my_list)):
        if my_list[index:index + length] == sublist:
                return index,index + length
def test_replace_sublist(): #test function for replace_sublist
    assert replace_sublist([1,3,5],[1,3,5],[5,3]) == [5,3]
    assert replace_sublist([1,2,3,1,4,4,5,1,4,4],[1,4,4],[2,2]) == [1,2,3,2,2,5,2,2]
    assert replace_sublist([1,3,5,4,1,3,5],[1,3,5],[]) == [4]
    assert replace_sublist([1,2,3,4,5,6],[6],[7,8,9]) == [1,2,3,4,5,7,8,9]
    assert replace_sublist([1,2,3],[2],[1]) == [1,1,3]


def replace_sublist(my_list,sublist,replacement):
    '''
    Description :Replace a sublist with another sublist
    Data: my_list,sublist,replacement
    Precondition : my_list,sublist,replacement - lists
    '''
    length = len(replacement)
    index = 0
    for start, end in iter(lambda: find_first_sublist(my_list, sublist, index),None):
        my_list[start:end] = replacement
        index = start + length
    return my_list

test_replace_sublist()    

#Homework for lab 4

def test_prime() :  #test function for prime
    assert prime(7) == True
    assert prime(1) == False
    assert prime(2) == True
    assert prime(4) == False
    assert prime(31) == True

def prime(n) :
    '''
Description : Verifies if a number is prime
Data : n
Precondition : n natural number
Result : True - if the number n is a prime number 
         False - if the number n is not prime
'''
    if n < 2 :
        return False
    elif n == 2 :
        return True
    elif n % 2 == 0 :
        return False
    else :
        for i in range(3,int(math.sqrt(n)) + 1) :
            if n % i ==0 :
                return False
        return True

test_prime() 

def test_print_prime() :
    assert print_prime([1,4,2,3,5],1,2) == [2] 
    assert print_prime([4,6,8],0,0) == []
    assert print_prime([1,2,4,6],0,1) == [2]
    assert print_prime([1,3,5],0,2) == [3,5]

def print_prime(v,start,end) :
    '''
    Description : Prints the prime numbers from start to end
    Data :v,start,end
    Precondition : v -list,start&end natural numbers ,start<=end
    '''
    prime_list = []
    for index in range(start,end + 1) :
        if prime(v[index]) :
            prime_list.append(v[index])
    return prime_list

test_print_prime()

def test_odd_number() : #tets function for odd_number
    assert odd_number(2) == False
    assert odd_number(3) == True
    assert odd_number(1) ==True
    assert odd_number(100) == False
    assert odd_number(71) == True

def odd_number(n) :
    '''
Description : Verifies if a number is odd
Data : n
Precondition : n narutal number
Result : True if n is an odd number
         False if n is an even number
'''
    if n & 1 :
        return True
    else :
        return False

test_odd_number()

def test_print_odd() :
    assert print_odd([1,2,3],0,0) == [1]
    assert print_odd([1,5,6],0,1) ==[1,5]
    assert print_odd([2,4,6],0,2) == []
    assert print_odd([1,3,5],0,2) == [1,3,5]
    assert print_odd([1,4,6,8],3,3) == []



def print_odd(v,start,end) :
    ''' 
    Description :Prints the odd numbers from start to end
    Data :v,start,end
    Precondition :v-list,start&end natural numbers ,start<=end
    '''
    odd_list = []
    for index in range(start,end + 1) :
        if odd_number(v[index]) :
            odd_list.append(v[index])
    return odd_list

test_print_odd()

#Feature 4

def test_sum() : #test function for get_sum_range
    assert get_sum_range([1,2,3,4,5,6,7,8],1,3) == 9
    assert get_sum_range([1,2,3,4,5,6,7,8],0,1) == 3
    assert get_sum_range([1,2,3,4,5,6,7,8],1,2) == 5
    assert get_sum_range([1,2,3,4,5,6,7,8],2,3) == 7
    assert get_sum_range([1,2,3,4,5,6,7,8],3,4) == 9
def get_sum_range(v,start,end) :
    '''
Description : Print the sum o a subarray starting from 'start' until 'end'
Data : v,start,end
Precondition : v - list , start and end natural numbers , start <= end
'''
    return sum(v[start : end + 1]) 

test_sum()

def tets_gcd() : #test function for gcd
    assert gcd(2,3) == 1 
    assert gcd(2,4) == 2
    assert gcd(10,100) == 10
    assert gcd(0,0) == -1
    assert gcd(1,1) == 1
def gcd(a,b) :
    '''
Description : Computes the gcd of tow natural numbers
Data : a,b
Precondition : a,b - natural numbers
Result : gcd(a,b)
'''
    if a == 0 :
        if b == 0 :
            return -1
        else :
            return b
    else :
        if b == 0 :
            return a
        else :
            while a != b :
                if a > b :
                    a = a - b
                else :
                    b = b - a
            return a

tets_gcd()

def get_gcd_range(v,start,end) :
    '''
Description : Returns the gcd from 'start' to 'end'
Data :v,start,end
Precondition : v-list ,start and end natural numbers, start < end
'''
    k = gcd(v[start],v[start + 1])
    for i in range(start + 2,end + 1) : 
        k = gcd(v[i],k)
    return k

def test_get_max_range() : #test function for get_max_range
    assert get_max_range([1,2,3,4,5],0,2) == 3
    assert get_max_range([11,1,3,5,6],0,4) == 11
    assert get_max_range([12,1,2,3,5,13,0,14],0,7) == 14
    assert get_max_range([1,2,3,4,5],2,3) == 4
    assert get_max_range([1,2,3,4,5],0,4) == 5
    assert get_max_range([1,2,3],0,0) == 1
    assert get_max_range([1,2,3],2,2) == 3

def get_max_range(v,start,end) :
    '''
Description : Returns max from start to end
Data : v,start , end
Precondition : v -list ,start&end natural numbers
Result : max(v[start : end])
'''
    return max(v[start : end + 1])

test_get_max_range()

def test_filter_primes(): #Testfunction for filter primes 
    assert filter_primes([1,2,3]) == [2,3]
    assert filter_primes([4,6,8]) == []
    assert filter_primes([5,11,8,9,10,21]) == [5,11]
    assert filter_primes([0,1,2]) == [2]
    assert filter_primes([0,0,0]) == []

def filter_primes(v):
    '''
    Description : Return v with only primes numbers
    Data : v
    Precondition : v-list
    '''
    v = [elem for elem in v if isPrime(elem)]
    return v

test_filter_primes()

def isNegative(n):
    '''
    Description : Checks if a number is negative
    Data : n
    Precondition : n - integer number
    Result : True if n < 0
            False if n > 0
    '''
    if n < 0 :
        return True
    else :
        return False

def test_negative_numbers(): #test function for filter_negative_numbers
    assert filter_negative_numbers([1,2,3]) == []
    assert filter_negative_numbers([0,-1,-2]) == [-1,-2]
    assert filter_negative_numbers([-1,-2,-11,-12]) == [-1,-2,-11,-12]
    assert filter_negative_numbers([0,0,0]) == []
    assert filter_negative_numbers([-1])  == [-1]
    
def filter_negative_numbers(v):
    '''
    Description : Keeps in a list only negative numbers
    Data : v
    PRecondition : v -list
    '''
    
    v = [elem for elem in v if isNegative(elem)]
    return v

test_negative_numbers()

def read_from_files(l) :
    try :
        fin = open("input.txt", "r")
        my_list = []
        all_lines = fin.read()
        lines = all_lines.split("\n")
        for line in range(1,len(lines)-2) :
            my_list.append(int(line))
        l = my_list[:]
    except ValueError as ex1 :
        print("Something is wrong as value...", str(ex1))
    except IOError as ex2 :
        print("Something is wrong as IO..." + str(ex2))
    finally :
        fin.close() 
    return l      

def write_to_file(l) :
    try :
        fout = open("output.txt","w")
        fout.write(str(l))
    except IOError as ex1 :
        print("Something is wrong as IO..." + str(ex1))
    except ValueError as ex2 :
        print("Something is wrong as value...", str(ex2))
    finally :
        fout.close()

