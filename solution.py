def Solution(A, D):
# define variables for items we will need in our code
    balance = 0
    fees = 0
    card_payments = 0
    card_payments_amount = 0
    date = D[i].split("-")

  # Iterate through the list A to find trasanctions less than 0 and add the to the card payments count.
    for i in range(len(A)):
        if A[i] < 0:
            card_payments += 1
            card_payments_amount += A[i]
        else:
            balance += A[i]
            if card_payments >3 and card_payment_amount >= -100:
                fees += 5
                card_payments = 0
                card_payment_amount = 0
            else:
                fees += 5
                card_payments = 0
                card_payment_amount = 0
                balance -= 5
    if card_payments >= 3 and card_payment_amount >= -100:
        fees += 5
    return balance - fees
  

print(Solution([1,-1,0,-105,1],["2020-12-31","2020-04-04","2020-04-14","2020-07-12"]))
