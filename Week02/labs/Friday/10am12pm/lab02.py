from random import randint

targetNumber = randint(1, 100)
tries = 0
maxtries = 10

def isClose(userInput):
    if (targetNumber - userInput <= 5 and targetNumber - userInput >= -5):
        print("You're very close!")

while True:
    print("Would you like to play?")
    playing = input().strip().lower()
    if (playing == "yes"):
        break
    elif (playing == "no"):
        print("Maybe next time!")
        exit(0)
        

while tries < maxtries:
    print("Guess a number: ", end="")
    try:
        userGuess = int(input())
        if (userGuess < 1 or userGuess > 100):
            raise ValueError
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 100.")
        continue

    if (userGuess == targetNumber):
        print(f"Congratulations! You guessed it in {str(tries)} attempts!")
        exit(0)
    elif (userGuess > targetNumber):
        print("Too high!. Try again")
        isClose(userGuess)
    elif (userGuess < targetNumber):
        print("Too low!. Try again")
        isClose(userGuess)
        
    tries += 1

print(f"Game over! The target number was {str(targetNumber)}.")