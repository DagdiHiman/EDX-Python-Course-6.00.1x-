s="Hibob Bobob bo b"
count=0
x=0; y=3
length = int(len(s))
while y < length:
    z=s[x:y]
    if (z=='bob'):
        count+=1
    else :
        count+=0
    y+=1
    x+=1
print("No. of bob =" + str(count))

"""
#another method-
s="Hibob Bobob bo bob"
numBobs = 0
for i in range(1, len(s)):
    if s[i:i+3] == 'bob':
        numBobs += 1
print("No. of bob =" + str(numBobs))
"""