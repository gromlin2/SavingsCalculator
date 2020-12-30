import math

from prettytable import PrettyTable

initial_net_worth = input("Initial net worth: ")
monthly_saving = input("What do you save per month: ")
expected_interest_rate = input("Expected interest rate: ")

current_net_worth = initial_net_worth
current_net_worth_with_interest = initial_net_worth
monthly_interest_rate = math.pow(1 + expected_interest_rate, 1.0 / 12.0) - 1

print("-----")
print("Monthly rate: {}".format(monthly_interest_rate))

t = PrettyTable(['Month', 'Month of year', 'Year', 'Invested', 'Total', 'Interest', 'Interest ratio'])
for i in range(0, 240):
    if i % 1 == 0:
        difference = current_net_worth_with_interest - current_net_worth
        interest_ratio = difference / current_net_worth_with_interest
        t.add_row([i, i % 12, i / 12, round(current_net_worth, 1), round(current_net_worth_with_interest, 1),
                   round(difference, 1), round(interest_ratio, 3)])
    current_net_worth = current_net_worth + monthly_saving
    current_net_worth_with_interest = current_net_worth_with_interest * (1.0 + monthly_interest_rate) + monthly_saving

print(t)
