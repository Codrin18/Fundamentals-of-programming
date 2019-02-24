'''
Created on Jan 5, 2019

@author: codrin18
'''
def sort_by_function(my_list,relation):

    k = 1
    isSorted = False

    while not isSorted :
        isSorted = True
        for i in range(len(my_list)-k):
            if relation(my_list[i],my_list[i+1]) is False:
                my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
                isSorted = False

        k = k + 1

    return my_list

def search_by_function(my_list,condition):

    res = []

    for el in my_list:
        if condition(el) is True:
            res.append(el)

    return res


def filter_by_function(my_list,condition):

    return list(filter(lambda x: condition(x),my_list))


def get_next(index):
    return index + 1

def initSolution(domain):
    return domain[0]

def isConsistent(sol,my_list,constraints):

    for c in constraints :
        if c(sol,my_list) is True :
            return False

    return True

def get_last(domain):
    return domain[len(domain)-1]

def isSolution(sol,param):
    return len(sol) == param[0]

def my_backtracking(param,my_list,condition):

    domain = [i for i in range(-1,len(my_list))]

    k = 0

    sol = []

    sol.append(initSolution(domain))

    while k >= 0 :

        isSelected = False
        while not isSelected and sol[k] < get_last(domain):
            sol[k] =  get_next(sol,my_list,condition)
            isSelected = isConsistent(sol,my_list,condition)

        if isSelected :
            if isSolution(sol,param):
                yield sol
            else :
                k = k + 1
                sol.append(initSolution(domain))

        else :
            sol.pop()
            k = k - 1
