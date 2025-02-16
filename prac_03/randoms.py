# What did you see on line 1?
# Answer: The randint module generates random number both 5 and 20 inclusive
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest possible number that could have been generated is 5.
# What did you see on line 2?
# Answer:The randrange(start, stop, step) module generates numbers starting at 3, increasing by 2, ending at 10.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number possible here is 3 and the largest number possible is 9.
# Could line 2 have produced a 4?
# Answer: Line 2 will never produce a 4, because after 3 the next number will be 5 here .
# What did you see on line 3?
# Answer:A random floating-point number between 2.5 and 5.5
# What was the smallest number you could have seen, what was the largest?
# Answer:The smallest number possible here is 2.5 , and the highest number possible is 5.5


# Write code to produce a random number between 1 and 100 inclusive.
import random
random_number=random.randint(1, 100)
print(random_number)
