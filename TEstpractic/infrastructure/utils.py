'''
Created on Jan 15, 2019

@author: codrin18
'''

def sort_by_function(my_list,fun):
    
    isSorted = False 
    k = 1
    while not isSorted:
        
        isSorted = True
        
        for index in range(len(my_list)-k):
            
            if fun(my_list[index],my_list[index+1]) is False :
                my_list[index],my_list[index+1] = my_list[index+1],my_list[index]
                isSorted = False
                
        k = k + 1
        
    return my_list
        
def sort_by_python(my_list,fun):
    
    
    return sorted(fun,my_list)