# Conditional
# Method evaluate data 
# if then else 

import random
high_range = 100
middle_num = int(high_range / 2)
my_guess = middle_num
number_guess = 0
my_rand_num = random.randint(1, high_range)
print(my_rand_num)
print(my_guess)


# evauluate the random number and compare it to middle number
if my_rand_num < my_guess:
    print(f'{my_rand_num} is less than {my_guess}')
elif my_rand_num == my_guess:
    print(f"{my_rand_num} is equal to {my_guess}")
else:
    print(f'{my_rand_num} is greater than {my_guess}')