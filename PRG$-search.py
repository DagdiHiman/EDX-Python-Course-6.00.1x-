print("Liniar Search")
count=0
key=int(input("Enter Key="))
for i in range(0, 100):
    if(key==i):
        print(i)
        count=1
        break
    
if count==1:
    print("FOund")
elif key>99 and key<0 :
    print("Try again")
else:
    print("Not Found")      