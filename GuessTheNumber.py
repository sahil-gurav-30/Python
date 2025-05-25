import random
 print("Name   : Sahil Gurav")
 print("USN    : 1AY24AI093")
 print("Section: O\n")
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
guess_count= 0
while True:
    print("Take a guess.")
    guess = int(input())  
    guess_count += 1
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Good job! You guessed my number in {guess_count} guesses!")
        break
