#COMPARE THE FOLLOWERS
#WRITE A SENTENCE FROM DICTIONARY
#IF WIN, THE WINNER BECOME OBJECT 1
#LOOP UNTIL FALSE
#RANDOM CHOICE FROM DATA LIST
import random

from game_data import data
from art import logo,vs


def sentence(ind):
    """Takes index to tranform the data into printable format"""
    return f"{data[ind]['name']}, {data[ind]['description']}, from {data[ind]['country']}."

def compare(guess, obj1, obj2):
    """Takes user's guess and compare object1 and object2"""
    if data[obj1]['follower_count'] > data[obj2]['follower_count']:
        return guess == "a"
    if data[obj1]['follower_count'] < data[obj2]['follower_count']:
        return guess == "b"
print(logo)
score = 0
object2 = random.randint(0, 49)
should_continue = True
while should_continue:
    object1 = object2
    object2 = random.randint(0, 49)
    if object1 == object2:
        object2 = random.randint(0, 49)
    print(f"Compare A: {sentence(object1)}")
    print(vs)
    print(f"Against B: {sentence(object2)}")
    user_guess= input("Who has more followers? 'A' or 'B'").lower()
    print("\n"* 20)
    print(logo)

    if compare(user_guess, object1, object2):
        score += 1
        print(f"You're right. Your current score is: {score}")
    else:
        print(f"Sorry, you're wrong!. Final Score: {score}")
        should_continue = False






