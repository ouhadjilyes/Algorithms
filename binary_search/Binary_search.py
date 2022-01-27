#########################################################################

def binary_search(list_elements , item):

# low and high keep track of which part of the list you'll search in
    low = 0 
    high = len(list_elements)- 1
    #print("low: " ,low , "," , "high: " , high)

# while you haven't narrowed it down to one element...
    while low <= high:

        # ...check the middle element
        mid = (low + high)/ 2
        #print("mid: " , mid)
        guess = list_elements[int(mid)]
        
        #print("guess: " , guess) 
        # found the item
        if guess == item:
            return int(mid)

        #the guess was too high
        if guess > item:
            high = mid #- 1
            #print("high :",high)

        # the guess was too low
        else:
            low = mid #+ 1
    return None  # the item doesn't exist
my_list = [1, 3, 5, 7, 9 , 11, 13, 15, 17, 19, 21] 
print (binary_search(my_list, 13))
print (binary_search(my_list, 17)) 
