import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

def print_greeting():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def get_difficulty():
    difficulty = None
    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficulty

def set_difficulty():
    difficulty = get_difficulty()
    return 10 if difficulty == "easy" else 5

def main():
    print_greeting()

    answer = random.randint(1, 100)
    guesses = set_difficulty()

    while guesses > 0:
        print(f'You have {guesses} attempts remaining to guess the number.')

        guess = int(input('Make a guess: '))

        if guess == answer:
            print(f'You got it! The answer was {answer}.')
            return
        elif guess > answer:
            print('Too high.')
        else:
            print('Too low.')

        guesses -= 1
        if guesses == 0:
            print("You've run out of guesses. You lose")
        else:
            print('Guess again.')
    

if __name__ == "__main__":
    main()
    