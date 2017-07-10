n=4
s=10
import math

"""def polysum(n,s):
   
    input is two ints or floats n and s
    output is area plus square of perimeter for regular polygon with n sides and side length s
    
    area = (0.25*n*(s**2))/(math.tan(math.pi / n))
    perimeter = n*s
    return round(area + perimeter**2,4)
"""def polysum(n,s):
    #pi=22/7
    import math
    print("area of regular polygon=")
    area= (0.25*n*(s**2))/math.tan(math.pi/n)
    peri= (n*s)**2
    sum= area+peri
    return(round(sum,4))
    #return("%.4f" % sum)
    #return sum
ar= polysum(n,s)
print(ar)   
        #561728.8315+123201