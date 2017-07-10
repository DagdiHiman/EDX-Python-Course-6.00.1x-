# string 
str = "azcbobobeghakl"
st=''
i = 0
count = 1
count_char = 0
while i < len(str)-1:
   
       first = str[i]
       second = str[i+1]
       
       #print(first)
       #print(second)
       
       print("***1***")
       if count_char < len(str)-1:
           count_char += 1
       print("***2***")
       count = 1
       
       while ord(first) < ord(second):
           count += 1
           i+=1
           st+=first
           print("***3***")
           #print(st ," Only ")
           if i < len(str)-1:
               first = str[i] 
               second = str[i+1]
               
               #print(first)
               #print(second)
               
           else:
               print("Count is (inside) ", count)
               print(st,first)
               st = ""
               #count = 1
               break      
           
       print("Count is (outside) ", count)
       print(st,first)
       st = ""
       i = count_char