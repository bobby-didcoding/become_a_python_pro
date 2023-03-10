
import random
import math

#get int range
lower = input("Enter Lower int:- ")
if not isinstance(lower, int):
    raise Exception("Please supply an integer")
upper = input("Enter Upper int:- ")
if not isinstance(upper, int):
    raise Exception("Please supply an integer")

 
#generate random number between lower & upper
answer = random.randint(lower, upper)#

#calculate alloted chances
chances = round(math.log(upper - lower + 1, 2))
print(f'You only have {chances} chances to guess the integer!')

# Initializing the number of guesses.
count = 0
#Loop whilst count <= chances
while count < chances:
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if answer == guess:
        if count > 1:
            attempts = "attempts"
        else:
            attempts = "attempts"
        print(f'Congratulations. You did it in {count} {attempts}.')
        break
    elif answer > guess:
        print("Your guess was too small")
    elif answer < guess:
        print("You guess was too high")
 
# Run out of guesses
if count >= chances:
    print(f'The number is {answer}, better luck next time')