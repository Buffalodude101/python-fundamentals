# Conditional
# Method evaluate data 
# if then else 

#ask user to select upper bound
#ask the user to guess

import random


#check if upper bound is valid
upper_bound = int(input("What is the upper bound? "))


#generate a random integer starting at 1 and going to upper bound
random_number = random.randint(1, upper_bound)
print(random_number)

user_guess = None
number_of_guesses = 1
while user_guess != random_number:

#ask user to guess
    user_guess = int(input(f"What is your guess from 1 to {upper_bound}: "))
  
    if user_guess == random_number:
        print("You win!!")
        #exit the loop
    # User guess is != to random number
    else:
        print("You lose")
        number_of_guesses += 1

print(f"Game over you took {number_of_guesses} tries")


# high_range = int(input(''))
# middle_num = int(high_range / 2)
# my_guess = middle_num
# number_guess = 0
# my_rand_num = random.randint(1, high_range)
# print(my_rand_num)
# print(my_guess)


# # evauluate the random number and compare it to middle number
# if my_rand_num < my_guess:
#     print(f'{my_rand_num} is less than {my_guess}')
# elif my_rand_num == my_guess:
#     print(f"{my_rand_num} is equal to {my_guess}")
# else:
#     print(f'{my_rand_num} is greater than {my_guess}')