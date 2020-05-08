#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    
    for i in range(len(list1)):
        if list2[len(list2) - 1 - i] == None:
            str1 = list1[i]
        elif list1[i] == None:
            str1 = list2[len(list2) - 1 - i]
        else:
            str1 = list1[i] + list2[len(list2) - 1 - i]
            
        merged_data += str1
        if i<len(list1)-1:
            merged_data+=" "
        
    resultant_data = merged_data
    return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)