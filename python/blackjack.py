import os
import random
import sys

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

def get_decision(message):
    decision = None
    while decision != 'y' and decision != 'n':
        decision = input(message)
    return decision

def get_player_starting_decision():
    return get_decision("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def get_player_decision():
    return get_decision("Type 'y' to get another card, type 'n' to pass: ")

def should_start_game():
    return True if get_player_starting_decision() == 'y' else False

def should_player_get_another_card():
    return True if get_player_decision() == 'y' else False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10]
    return random.choice(cards)

def deal_starting_hand():
    hand = []
    for i in range(2):
        hand.append(deal_card())
    return hand

def calculate_score(hand):
    score, aces = 0, 0
    for card in hand:
        score += card
        if card == 11:
            aces += 1
    while score > 21 and aces > 0:
        hand.remove(11)
        hand.append(1)
        aces -= 1
        score -= 10
    return score

def compare_scores(player_score, computer_score):
    if player_score > 21:
        return 'You went over. You lose.'
    if player_score == computer_score:
        return 'You draw.'
    elif computer_score == 21:
        return 'You lose, your opponent has a Blackjack.'
    elif player_score == 21:
        return 'Congratulations, you win with a Blackjack!'
    elif computer_score > 21:
        return 'The opponent went over. You win!'
    elif player_score > computer_score:
        return 'You win!'
    else:
        return 'You lose.'

def clear():
    os.system('clear')

def main():
    while should_start_game():
        clear()
        print(logo)

        player_hand = deal_starting_hand()
        computer_hand = deal_starting_hand()
        game_over, player_turn = False, True

        while not game_over:
            player_score = calculate_score(player_hand)
            computer_score = calculate_score(computer_hand)
            if player_score >= 21 or computer_score >= 21:
                break
            if player_turn:
                print(f'Your cards: {player_hand}, current score: {player_score}')
                print(f"Computer's first card: {computer_hand[0]}")
                if should_player_get_another_card():
                    player_hand.append(deal_card())
                else:
                    player_turn = False
            elif computer_score < 17:
                computer_hand.append(deal_card())
            else:
                game_over = True
        print(f'Your final cards: {player_hand}, final score: {player_score}')
        print(f"Computer's final cards: {computer_hand}, final score: {computer_score}")
        print(compare_scores(player_score, computer_score))
    
    sys.exit(0)

if __name__ == "__main__":
    main()