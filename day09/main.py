import os
import art

print(art.logo)

bids = {}
bidding_is_on = True

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_is_on:
    name = input("What's your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_is_on = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_screen()
        