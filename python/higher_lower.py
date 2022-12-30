import os
import random

from game_data import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def clear():
    os.system('clear')

def display_logo():
    clear()
    print(logo)

def display_options(option_a, option_b, score):
    display_logo()
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

def generate_new_index(current_index, start, stop):
    new_index = random.randint(start, stop)
    while new_index == current_index:
        new_index = random.randint(start, stop)
    return new_index

def compare_followers(count_a, count_b):
    if count_a > count_b:
        return 'A'
    elif count_b > count_a:
        return 'B'
    else:
        return 'Tie'

def main():
    game_over = False
    score = 0
    option_a_index, option_b_index = None, None

    while not game_over:
        if not option_a_index:
            option_a_index = random.randint(0, len(data)-1)
        option_b_index = generate_new_index(option_a_index, 0, len(data)-1)

        option_a = data[option_a_index]
        option_b = data[option_b_index]

        display_options(option_a, option_b, score)

        player_choice = input("Who has more followers? Type 'A' or 'B': ")
        higher_option = compare_followers(option_a['follower_count'], option_b['follower_count'])
        
        if higher_option == 'Tie' or higher_option == player_choice:
            score += 1
            option_a_index = option_b_index
        else:
            game_over = True

    display_logo()
    print(f"Sorry, that's wrong. Final score: {score}")

if __name__ == "__main__":
    main()