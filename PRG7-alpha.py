#there is an error correct it :not printing last letter
s='abcd'
n=1;p=0
x=s[p]
y=s[p+1]
st=''
special=''
temp=0
char_temp=0

for letter in s:
    if(char_temp< len(s)-1):
        char_temp+=1

    count=1  
    x=letter
    y=(s[char_temp])
    
    print(n,"--> letter=",letter)
    n+=1
    while(ord(y)>ord(x)):
        count+=1
        p+=1
        if p < len(s)-1:
            x=s[p]
            y=s[p+1]
        else:
            break
        st+=s[p-1]
    p=char_temp
    st+=x
    if(count>temp):
        special=''
        temp=count
        special+=st
    print("\t:-", st)
    st='' 
    
print("FINAL")
print("MAX COUNT= ",temp , " & LONGEST STRING= ", special)
