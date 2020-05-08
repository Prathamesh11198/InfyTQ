#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    lst = []
    data = text.split(" ")
    for word in data:
        if word not in vocabulary:
            lst.append(word)
    
    if len(lst) > 0:
        return set(lst)
    else:
        return -1
    
#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)