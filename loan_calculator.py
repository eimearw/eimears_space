money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the apr?\n"))
payment = float(input("What will your monthly repayment be, in dollars?\n"))
months = int(input("How many months do you want to calculate for?\n"))
# Divide apr by 100 to get %, divide by 12
monthly_rate = apr/100/12

for i in range(months):
# Add interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest.", end="")
    print(" Now you owe", money_owed)
