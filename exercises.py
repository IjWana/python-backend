# Write a dice rolling game program
# Write a python program that keeps asking the user if they want to roll the dice,
# It should ask them to choose a yes/no or y/n as answer
# If the user inputs 'yes' or 'y', generate 2 random dice numbers,
# If the user enters another value rather than 'yes' or 'y' or 'no' or 'n',
# tell them 'Invalid choice!' and continue the game
# If the user inputs 'no' or 'n', tell them 'Thanks for playing!', then terminate the game.

# The thought process
# 1. Ask the user if they want to roll the dice?
#  2. If user enters 'yes' or 'y',:
#         generate 2 random dice numbers
#  print those numbers
#  3. If the user enters 'no' or 'n',:
# print game ended
#  else:
#  print invalid choice and input a valid choice and continue with the game.


# import random


# def roll_dice_game():
#     """A simple dice rolling game with user input validation."""
#     while True:
#         # Get and normalize user input
#         user_choice = input(
#             "Would you like to roll the dice? (y/n): ").lower().strip()

#         if user_choice in ['yes', 'y']:
#             # Roll two dice and print the results
#             dice1 = random.randint(1, 6)
#             dice2 = random.randint(1, 6)
#             print(f"Rolling the dice...")
#             print(f"The values are: {dice1} and {dice2}")
#         elif user_choice in ['no', 'n']:
#             # End the game
#             print("Thanks for playing!")
#             break  # Exit the loop to terminate the program
#         else:
#             # Handle invalid input
#             print("Invalid choice! Please enter 'yes', 'y', 'no', or 'n'.")


# # Start the game
# if __name__ == "__main__":
#     roll_dice_game()

#######################################
# import random

# while True:

#     user_input = input(
#         'Do you want to the roll the dice? (yes/no): ').lower().strip()

#     if user_input == 'yes':
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print(f"{dice1} and {dice2}")
#     elif user_input == 'no':
#         print('You are not interested!')
#         break
#     else:
#         print('Invalid choice')

##########################################
# Reversed A String
# user_input = input('Enter anything please: ')
# reversed_input = user_input[::-1]
# print("Reversed Input is:", reversed_input)

# Reversed a group of words - Method I
# statement = 'Python is a powerful programming language'
# words = statement.split()
# reversed_words = words[::-1]
# reversed_statment = " ".join(reversed_words)
# print(reversed_statment)

# Method II


# def reversed_sentence():
#     statement = input("Enter a sentence: ")
#     words = statement.split()
#     reversed_words = ' '.join(reversed(words))
#     print(f"The reversed statement is:", reversed_words)


# reversed_sentence()

# py -m venv venv - creat a virtual env
# venv\Scripts\activate - to activate the virtual env

# Write a python program that takes a URL and generate a QR code for the given url and save QR code in a file

# import qrcode


# data = input('Enter your URL: ')
# filename = input('Enter your preferred filename: ')
# qr = qrcode.QRCode(box_size=10, border=4)
# qr.add_data(data)
# image = qr.make_image(fill_color='black', back_color='white')

# image.save(filename)
# print(f"QR Code saved as {filename}")

##############################################
# Guess game
# Write a program to have the computer randomly select a number between 1 and
# 10, and then prompt the player to guess the number. The program should give
# hints if the guess is too high or too low.

import random


# def guess_the_number():
#     """
#     A number guessing game where the computer selects a number
#     and the user tries to guess it with hints.
#     """
#     # Generate a random number between 1 and 10
#     secret_number = random.randint(1, 10)

#     print("Welcome to the guessing game!")
#     print("I have selected a number between 1 and 10.")
#     print("Try to guess what it is.")

#     while True:
#         try:
#             # Prompt the user for their guess
#             guess = int(input("Enter your guess: "))

#             # Check if the guess is correct
#             if guess == secret_number:
#                 print(
#                     f"Congratulations! You guessed it. The number was {secret_number}.")
#                 break  # Exit the loop and end the game
#             elif guess < secret_number:
#                 print("Too low! Try a higher number.")
#             else:
#                 print("Too high! Try a lower number.")
#         except ValueError:
#             # Handle cases where the user enters non-integer input
#             print("Invalid input. Please enter a whole number.")


# # Start the game
# if __name__ == "__main__":
#     guess_the_number()

import random


def guess_the_number():

    guessed_number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Enter a number: "))
            if guess == guessed_number:
                print(f"Congratulations! You are correct. {guessed_number}")
                break
            elif guess < guessed_number:
                print("Wrong! Try again.")
            else:
                print("You can do better")
        except ValueError:
            print("Invalid Input. Please enter a whole number.")


if __name__ == "__main__":
    guess_the_number()
