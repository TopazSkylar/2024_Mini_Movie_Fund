def cash_credit(question):

    while True:
        response = input(question).lower()
        # checks user response to question
        # only accepts yes or no
        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please choose a valid payment method ")


# main routine goes here
while True:
    payment_method = cash_credit("Choose a payment method (cash or credit)")
