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


# main routine goes here
instructions = yes_no("Do you want to read the instructions? ")

if instructions == "yes":
    print("Instructions go here")

print("done done")
