import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# 1
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?

# Line one produced random numbers from 5 to 20.

# 2
# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?

# On line two the code produced random numbers from 3 to 10 and only included odd numbers
# as range was from 3 to 10 in steps of 2.
# It couldn't produce 4 as it was not within the range function.

# 3
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?

# Line three produced a decimal with  up to 16 charters including numbers from 2.5 to 5.5
# was not restricted to only 1 decimal place

print(random.randint(1, 100))
