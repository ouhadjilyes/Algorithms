################################

#This is a function to count the number of items in a list :

def length(list):
    if list == []:
        return 0
    
    return 1 + length(list[1:])

print(length([1,3,34,23]))
    
