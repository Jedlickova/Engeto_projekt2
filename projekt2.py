"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Monika Jedličková
email.mcmilica@centrum.cz
discord: monika_64143
"""
import random
import time
from datetime import datetime, timezone

def print_link():
    link = "-" *49
    print(link)

def wrap_text(text, max_length=50):
    wrapped_text = ""
    if len(text) > max_length:
        cut_position = text.rfind(' ', 0, max_length)
        wrapped_text = text[:cut_position] + "\n" + text[cut_position + 1:]
    else:
        wrapped_text = text
    return wrapped_text

def generate_four_digit_number():
    four_digits = random.sample(range(10), 4)
    if four_digits[0] == 0:
        index = random.randint(1,3)
        four_digits[0], four_digits[index] = four_digits[index], 0
    four_digit_number = ""
    for digit in four_digits:
        four_digit_number += str(digit)
    return four_digit_number

def get_user_number():
    requirement = True
    while requirement:
        user_number = input("Enter a four-digit number:")
        if not user_number.isdigit():
            print(wrap_text("Invalid input, the number contains non-numeric characters."))
            print_link()
        elif len(user_number) != 4:
            print(wrap_text("Invalid input, the number is not four-digit number."))
            print_link()
        elif user_number[0] == "0":
            print(wrap_text("Invalid input, the number starts with zero."))
            print_link()
        elif len(set(user_number)) != len(user_number):
            print(wrap_text("Invalid input, the number contains a duplicate."))
            print_link()
        else:
            requirement = False
    return user_number

def compare_numbers(four_digit_number, user_number):
    cows = 0
    bulls = 0
    pc = list(four_digit_number)
    user = list(user_number)
    for user_i in range(4):
        for pc_i in range(4):
            if user[user_i] == pc[pc_i]:
                if user_i == pc_i:
                    bulls += 1
                else:
                    cows += 1
    return bulls, cows

def choose_singular_or_plural(bulls, cows):
    if bulls == 1:
        bulls_text = "bull"
    else:
        bulls_text = "bulls"
    if cows == 1:
        cows_text = "cow"
    else:
        cows_text = "cows"
    return (f"{bulls} {bulls_text}, {cows} {cows_text}")

def print_result_message(attempts):
    if attempts == 1:
        guesses = "guess"
    else:
        guesses = "guesses"
    print(wrap_text(f"Correct, you've guessed the right number in {attempts} {guesses}!"))
    print_link()
    if attempts == 1:
         print("""That's unbelievable!""")
    elif attempts < 5:
        print("That's amazing")
    else:
        print("Good job.")
    print_link()

def format_time(length_time):
    time_obj = datetime.fromtimestamp(length_time, tz=timezone.utc)
    formatted_time = time_obj.strftime("%Hh %Mm %Ss")
    print(f"It took {formatted_time}.")


def play_game():
    start = time.time()
    pc_number = generate_four_digit_number()
    attempts = 0
    bulls = 0
    cows = 0
    while bulls < 4:
        user_number = get_user_number()
        print(f">>> {user_number}")
        attempts += 1
        bulls, cows = compare_numbers(pc_number, user_number)
        result = choose_singular_or_plural(bulls, cows)
        print(result)
        print_link()
    print_result_message(attempts)
    length_time = time.time() - start
    format_time(length_time)

print("Hi, there!")
print_link()
print(wrap_text("""I have generated a random 4 digit number for you. Let's play a bulls and cows game."""))
print_link()
print("Enter a number:")
print_link()

play_game()