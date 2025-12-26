import random as rd
loan_amount=5733000#float(input("Enter loan amount:\n"))
intRate=7.9#float(input("Annual interest rate:\n"))
pay_month=50400#float(input("How much will you pay this month:\n"))
months=240#float(input("How many months do you want to see the results for?\n"))

monthly_rate = intRate/12/100

for i in range(months):
    
    int_paid=loan_amount*monthly_rate
    loan_amount=loan_amount+int_paid
    loan_amount=loan_amount-pay_month
    if loan_amount<0:
        print("The last EMI is:",loan_amount)
        print("Paid in:",i+1," months")
        break
