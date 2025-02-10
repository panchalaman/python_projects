from art import logo
import random

def game():
    print(logo)
    print("I have chosen a number between 1 and 100, it's your time to guess now!")
    COM_NUM = random.choice(range(1, 100))

    def compare(num1, COM_NUM):
        if num1 == COM_NUM:
            print(f"Computer number: {COM_NUM}, YOU WIN!")
            return True
        elif num1 > COM_NUM:
            print("Too High")
            return False
        else:
            print("Too Low")
            return False

    def guess_loop(num):
        should_continue = True
        while should_continue:
            print(f"Remaining attempts: {num}")
            user_guess = int(input("Guess a number: "))
            result = compare(user_guess, COM_NUM)
            if not result:
                num -= 1
            elif num == 0:
                print("Attempts over! You lose!")
                should_continue = False
            if result:
                should_continue = False

    user_level = input("Choose a level:'hard' or 'easy' ").lower()
    if user_level == "hard":
        attempt = 5
        guess_loop(attempt)
    else:
        attempt = 10
        guess_loop(attempt)


game()
while input("Do you want to play again 'y' or 'n'") == "y":
    print("\n" * 30)
    game()
