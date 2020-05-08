#DSA-Tryout

import random
from timeit import default_timer as timer

def find_it_linear(num,element_list):
    #remove pass and copy the code written earlier for linear search
    guesses = 0
    for ele in element_list:
        if num == ele:
            return guesses
        else:
            guesses += 1

def find_it_binary(num,element_list):
    #remove pass and copy the code written earlier for binary search
    min1 = 0
    max1 = len(element_list)-1
    guesses = 0
    while(max1 >= min1):
        mid = (min1+max1)//2
        if num == element_list[mid]:
            return guesses
        elif element_list[mid] > num:
            guesses += 1
            max1 = mid - 1
        elif element_list[mid] < num:
            guesses += 1
            min1 = mid + 1
    return -1

#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    list_of_elements=initialize_list_of_elements(n)
    rand_index=random.randrange(0,len(list_of_elements))
    rand_num=list_of_elements[rand_index]
    print("Number to be guessed:",rand_num)
    start=timer()
    print("No. of guesses made using linear search:",find_it_linear(rand_num,list_of_elements))
    end=timer()
    print("Linear Search:Execution time in seconds:{0:.5f}".format( (end-start)))
    start=timer()
    print("No. of guesses made using binary search:",find_it_binary(rand_num,list_of_elements))
    end=timer()
    print("Binary Search:Execution time in seconds:{0:.5f}".format( (end-start)))

#Pass different values to play() and observe the output
play(40000)