import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print(logo)
    print('Welcome to the secret auction program.')
    end_auction = False
    bids = {}
    highest_bid = highest_bidder = None
    while not end_auction:
        name = input('What is your name?: ')
        bid = int(input('What is your bid?: $'))
        bids[name] = bid

        if highest_bid is None or bid > highest_bid:
            highest_bid = bid
            highest_bidder = name
        
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if more_bidders == 'no':
            end_auction = True
        else:
            clear()

    print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')

if __name__ == "__main__":
    main()