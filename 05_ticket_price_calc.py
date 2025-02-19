# functions go here
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this cannot be blank, please try again")
        else:
            return response

def int_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


def string_checker(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or then, letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # checks user response to question
            # only accepts yes or no
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item


# Main routine

# initialise variables / non-default options for string checker
payment_list = ("cash", "credit")

# Ticket Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

tickets_sold = 0

while True:

    name = not_blank("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = int_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print(f"{name} is too young")
        continue
    # ticket is $7.50 for users under 16
    if 12 <= age < 16:
        price = CHILD_PRICE

    # ticket is $10.50 for users between 16 and 64
    elif 16 <= age < 65:
        price = ADULT_PRICE

    # ticket price is $6.50 for seniors (65+)
    elif 65 <= age <= 121:
        price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    pay_method = string_checker("Payment method: ", payment_list, 2)

    if pay_method == "cash":
        surcharge = 0

    # calculate 5% surcharge if users are paying using credit
    else:
        surcharge = price * CREDIT_SURCHARGE

    # calculate total payable
    total_to_pay = price + surcharge

    print(f" Age: {age}, Ticket Price: ${total_to_pay:.2f}")

    tickets_sold += 1

# # loop for testing
# while True:
#     # Get age (assume users input a valid integer)
#     age = int(input("Age: "))
#
#     # calculate ticket cost
#     ticket_cost = calc_ticket_price(age)
#     print(" Age: {}, Ticket Price: {:.2f}".format(age, ticket_cost))
