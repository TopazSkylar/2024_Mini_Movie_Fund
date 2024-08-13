# functions go here

# checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this cannot be blank, please try again")
        else:
            return response


# checks that the user inputs an integer
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):
    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# checks that users enter a valid response (yes/no, cash/credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# main routine goes here

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# ask user if they want to see the instructions
instructions = string_checker("Do you want to read the instructions? ")

if instructions == "yes":
    print("Instructions go here")

print()
# set maximum number of tickets below

# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit : ")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again")
        continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)

    # get payment method
    for case in range(0, 5):
        pay_method = string_checker("Choose a payment method (cash/credit)", 2, payment_list)
        print("You chose", pay_method)

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There are {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
