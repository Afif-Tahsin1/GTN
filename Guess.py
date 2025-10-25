import random
lower_bound = int(input("Please enter your lower bound: "))
higher_bound = int(input("Please enter your higher bound: "))
max_attempts = 12
random_n = random.randint(lower_bound, higher_bound)
def get_guess():
    while True:
        guess = int(input(f"Please enter a number beetween {lower_bound} and {higher_bound}:"))
        if lower_bound <= guess <= higher_bound:
            return guess
        else:
            print(f"You entered a invalid number. Please enter a number beetween {lower_bound} and {higher_bound}")

def check_guess(guess, random_n):
    if guess == random_n:
        return "Correct"
    elif guess > random_n:
        return "Too high"
    else:
        return "Too low"

def play_game():
    attemps = 0
    won = False
    while attemps <= max_attempts:
        attemps += 1
        guess = get_guess()
        result = check_guess(guess, random_n)
        if result == "Correct":
            print(f"You guess the secret number {random_n} in attempts {attemps}!")
            won = True
            break
        else:
            print(f"{result} Try again")
    
    if not won:
        print(f"Sorry, you have failed the game, the secret number is {random_n}")

print("Welcome to the number guessing game!")
play_game()