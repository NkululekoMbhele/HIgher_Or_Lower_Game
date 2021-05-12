import random
import art
import game_data
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def format_account(account):
    """Takes account and return formated string"""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, accountA, accountB):
    """Check if answer is correct and return true otherwise false"""   
    if accountA['follower_count'] > accountB['follower_count']:
        return guess == "a"
    else:
        return guess == "b"
    

score = 0
game_live = True
print(art.logo)
while game_live:
    celebA = random.choice(game_data.data)
    celebB = random.choice(game_data.data)
    print(f"Compare A: {format_account(celebA)}")
    print(art.vs)
    print(f"Against B: {format_account(celebB)}")
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()   
    clearConsole()
    print(art.logo)
    if check_answer(user_input, celebA, celebB):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_live = False


