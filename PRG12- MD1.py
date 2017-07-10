def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    i = 1
    j = 0
    #for j in range(0, k, 1):
    while j < k:
        j = j + i
        i+=1
        
    if j == k:
        return True
    else:
        return False
        
    
            
g=is_triangular(2)
print(g)