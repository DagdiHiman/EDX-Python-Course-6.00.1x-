print("Please think of a number between 0 and 100! ")
x= 100
count= 0
low= 0
high= x
med=int(( low + high ) / 2)

while (low<=high):
    print("Is your secret number ", med)
    guess=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    count+=1
    if(guess == 'h'):
        high=med
    elif( guess == 'l'):
        low=med
    elif( guess == 'c'):
        print("Game over. Your secret number was: ", med)
        break
    else:
        print("Sorry, I did not understand your input.")
    med=int(( low + high ) / 2)
        