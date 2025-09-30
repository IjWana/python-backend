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
def reversed_sentence():
    statement = input("Enter a sentence: ")
    words = statement.split()
    reversed_words = ' '.join(reversed(words))
    print(f"The reversed statement is:", reversed_words)


reversed_sentence()
