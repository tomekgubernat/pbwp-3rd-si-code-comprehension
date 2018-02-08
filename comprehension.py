import random   # use module random

guesses_taken = 0 #assign 0 to global variable

print('Hello! What is your name?') #shows string on the screen
myName = input() #assign input data string to variable

number = random.randint(1, 20) #assign random integers use module random
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #add variable to string

while guesses_taken < 6: #loop True when variable is less than 6
    print('Take a guess.') #shows string
    guess = input() #assign input data string to variable
    guess = int(guess) #conversion variabe to integers numbers

    guesses_taken += 1 #updating a variable by adding 1 (increment)

    if guess < number: #condition to compare variables
        print('Your guess is too low.') #shows string

    if guess > number: #condition to compare variables
        print('Your guess is too high.') #shows string

    if guess == number: #check both variables is they equal
        break #stop the loop

if guess == number: #check both variables is they equal
    guesses_taken = str(guesses_taken)
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #add variable to string

if guess != number: #check both variables is they not equal
    number = str(number) #conversion variabe to string
    print('Nope. The number I was thinking of was ' + number) #add variable to string
