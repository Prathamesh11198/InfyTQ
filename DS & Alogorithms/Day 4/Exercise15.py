#DSA-Exer-15

def pattern_search(text, pattern):
    #Remove pass and write your logic here
    return text.count(pattern)

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)