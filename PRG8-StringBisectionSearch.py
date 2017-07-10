char='h'
aStr='acefjklvx'

#print(midIndex)
def isIn(char, aStr):
    if( if aStr == ''):
        return False
    if len(aStr) == 1:
      return aStr == char
    low = aStr[0]
    high = aStr[-1]
    ln=len(aStr)
    midIndex=int(ln/2)
    med= aStr[midIndex]
    #print("func")
    while(med != char and ord(low) <= ord(high)):
        #print("while")
        #print(med, char)
        if(ord(char) < ord(med)):
            #print("if")
            return isIn(char, aStr[:midIndex])
        else:
            #print("else")
            return isIn(char, aStr[midIndex+1:])
        med= aStr[midIndex]
    if(med == char):
        #print("if2")
        return True
    else:
        return False
lat=isIn(char,aStr)   
print(lat) 
    