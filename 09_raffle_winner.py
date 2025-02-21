import random
import pandas


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# dictionaries to hold ticket details
all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 6.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharges
}

# mini_movie_frame = mini_movie_frame.set_index('Name')
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# print(mini_movie_frame)
print(mini_movie_frame.to_string(index=False))

# Choose a winner from a name list
winner_name = random.choice(all_names)

# find index of winner (ie. position in list)
winner_index = all_names.index(winner_name)
print("winner", winner_name, "list position", winner_index)

# look up total amount won (ie: ticket price + surcharge)
winner_ticket_price = all_ticket_costs[winner_index]
winner_surcharge = all_surcharges[winner_index]

# total won
total_won = winner_ticket_price + winner_surcharge

print()
print('---- Raffle Winner ----')
print(f" Congrats {winner_name}. Their ticket of ${total_won:.2f} is free!")


