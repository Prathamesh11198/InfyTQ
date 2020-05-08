#DSA-Tryout
import random
def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using binary search algorithm
    #Return the total number of guesses made
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
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.
    lst = initialize_list_of_elements(n)
    rand_index=random.randrange(0,len(lst))
    rand_num = lst[rand_index]
    print(find_it(rand_num, lst))


#Pass different values to play() and observe the output
play(20)