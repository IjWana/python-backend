# Function is a reusable block of code that performs a specific task.
# def greeting():
#     print('Hello, Prince')


# greeting()

# Generic function
# def greeting(first_name, last_name):
#     print('Hello!', first_name, last_name)
#     print(f"Welcome back! {first_name} {last_name}")


# greeting('Ijoh', 'Emmanuel')

# def sum_two_numbers(num1, num2):
#     result = num1 + num2
#     print(result)


# sum_two_numbers(10, 10)

# def sum_two_numbers(num1, num2):
#     return num1 + num2


# result = sum_two_numbers(10, 10)
# print(result)


#########################################
# def user_grade(grade1, grade2):
#     return (grade1 + grade2) / 2


# result = user_grade(10, 100)
# if result > 60:
#     print('Very Good')
# elif result > 50:
#     print('Good')
# else:
#     print('Repeat the subject')


#############################################
# def user_grade2(grade1, grade2):
#     subj_grade = (grade1 + grade2) / 2

#     if subj_grade > 70:
#         print('Excellent')
#     elif subj_grade < 50:
#         print('Good')
#     else:
#         print('Repeat the subject.')


# user_grade2(10, 100)

# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     print(n * 2)


# salaries = [200000, 100000, 300000]

# for salary in salaries:
#     print(salary + (salary * 0.25))

# salaries = [200000, 100000, 300000]
# increment = []

# for salary in salaries:
#     new_salary = salary + (salary * 0.25)
#     increment.append(new_salary)
#     print(increment)


# ------------- LIST COMPREHENSION ------------------
# values = [10, 20, 30]
# new_values = [value * 2 for value in values]
# print(new_values)


# Manual Looping
# values = [10, 20, 30]
# new_values = []

# for value in values:
#     result = value * 2
#     new_values.append(result)

# print(new_values)

# -------- BUILT-IN MODULES AND LIBRARIES ----------------
# Math (Mathematics Operation)
# import math

# print(math.factorial(5))
# print(math.sqrt(81))
# print(math.pi)

# Random
# import random

# print(random.randint(1, 10))

# fruits = ['banana', 'apple', 'cherry']
# print(random.choice(fruits))

# Datetime (date and time)
from datetime import datetime
print(datetime.now())
