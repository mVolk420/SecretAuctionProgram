print("Welcome to the secret auction programm")
auction_bids = {}

while True:
    name = input("what is your name? ")
    bid = int(input("What ist your bid ? "))
    auction_bids[name] = bid

    get_all_bidders = int(input("are there any other bidders? Type 0 for no and 1 for yes"))
    if get_all_bidders == 0:
        break
winner_key = next(iter(auction_bids))
for key in auction_bids:
    winner_key = key
    if auction_bids[key] > auction_bids[winner_key]:
        winner_key = key

print("Winner is: " + winner_key + " with bid: " + str(auction_bids[winner_key]))