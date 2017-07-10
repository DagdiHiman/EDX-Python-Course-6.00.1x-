def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number
    of times in L. If no such element exists, returns None """
    occurence = {}
 
    for n in L:
        if n in occurence.keys():
            occurence[n] += 1
        else:   
            occurence[n] = 1
 
    copy = {}
    for k in occurence.keys():
        if occurence[k] % 2 != 0:
            copy[k] = occurence[k]
 
    if len(copy.keys()) == 0:
        return None
    else:
        return max(copy.keys())
 
 
print(largest_odd_times([2,2,4,4]))
print(largest_odd_times([3,9,5,3,5,3]))