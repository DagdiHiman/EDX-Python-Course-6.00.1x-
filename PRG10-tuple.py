def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    tup = ()
    count = 1
    for i in aTup:
        count += 1
        if(count % 2 == 0):
            tup += i  
    
    return tup
t = oddTuples(aTup)

            
