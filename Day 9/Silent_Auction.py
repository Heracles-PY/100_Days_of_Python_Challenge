from Gavel_Art import gavel_art
print(gavel_art)
print("Welcome to the Silent Auction!")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue_bidding = input("Would you like to continue? (y/n) ")
    if should_continue_bidding == "n":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue_bidding == "y":
        print("\n" * 20)