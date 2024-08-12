# functions go here

# checks for yes and no answers to questions
def yes_no(question):
    while True:
        response = input(question).lower()
        # checks user response to question
        # only accepts yes or no
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes or no ")


# checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this cannot be blank, please try again")
        else:
            return response


# main routine goes here

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# ask user if they want to see the instructions
instructions = yes_no("Do you want to read the instructions? ")

if instructions == "yes":
    print("Instructions go here")

print()
# set maximum number of tickets below

# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit : ")

    tickets_sold += 1

    if name == 'xxx':
        break

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There are {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
