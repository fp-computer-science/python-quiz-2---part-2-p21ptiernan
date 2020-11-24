# Author PT 11/24/20

import random 

lucky = str(input("Pleae input your three lucky numbers. "))

first = random.randrange(0, 50)
second = random.randrange(0, 50)
third = random.randrange(0, 50)


print("The winning numbers are {one}, {two}, {three}. Your numbers are {inpt}.".format(one=first, two=second, three=third, inpt=lucky))
