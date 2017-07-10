Previous_balance=int(input("Enter Balance= "))
Annual_interest_rate=int(input("Enter Annual_interest_rate= "))
Minimum_monthly_payment_rate= int(input("Enter Minimum_monthly_payment_rate= "))
h=int(input("number="))
def credit_card ( Previous_balance, n , Annual_interest_rate , Minimum_monthly_payment_rate ):
    
    if( n==1 ):
        return ( Previous_balance )
    else:
        Monthly_interest_rate= (Annual_interest_rate) / 1200
        Minimum_monthly_payment = (Minimum_monthly_payment_rate/ 100) * (Previous_balance) 
        Monthly_unpaid_balance = (Previous_balance) - (Minimum_monthly_payment)
        Previous_balance = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)       
        credit_card ( Previous_balance, n-1 , Annual_interest_rate , Minimum_monthly_payment_rate )

x=credit_card ( Previous_balance, h , Annual_interest_rate , Minimum_monthly_payment_rate )

print("Updated Outstanding Balance= ", x)