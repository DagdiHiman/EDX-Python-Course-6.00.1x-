x= 100
print("BINARY SEARCH")
count= 0
key=int(input("Enter Key="))
low= 0.0
high= x
med=( low + high ) / 2.0

while (key!= med and low<=high):
    
    count+=1
    if(key<med):
        high=med
    else:
        low=med
    med=( low + high ) / 2.0
        
if(med==key):
    print("key =", med)
    print("Total steps= ", count)
else:
    print("NOT FOUND!!")    