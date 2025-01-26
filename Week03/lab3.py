# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining
diceOptions = list(range(1,7))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
print("Available weapons:")
for w in weapons:
    print(w)

while True:
    combatStrength: int
    try:
        combatStrength = int(input("Enter your combat Strength: (Number between 1-6) "))
    except ValueError:
        print("Input must be an integer between 1-6")
        continue

    if(combatStrength < 1 or combatStrength > 6):
        print("Input must be an integer between 1-6")
    else:
        mCombatStrength: int
        try:
            mCombatStrength = int(input("Enter the monster's combat Strength: "))
        except ValueError:
            print("Input must be an integer between 1-6")
            continue
        
        if(mCombatStrength  < 1 or mCombatStrength > 6):
            print("Input must be an integer between 1-6")
        else:
            wins = 0
            mWins = 0
            for round in range(1, 20, 2):
                if (round == 11):
                    print("Battle truce")
                    break

                roll = random.choice(diceOptions)
                mRoll = random.choice(diceOptions)
                weapon = random.choice(diceOptions) - 1
                mWeapon = random.choice(diceOptions) - 1
                realCombatStrength = roll + (weapon + 1) + combatStrength
                mRealCombatStrength = mRoll + (weapon + 1) + mCombatStrength

                print(f"Round {round}: Hero rolled {roll}, Monster rolled {mRoll}.")
                print(f"Hero selected: {weapons[weapon]}, Monster selected: {weapons[mWeapon]}")
                print(f"Hero Total Strength: {realCombatStrength}, Monster Total Strength: {mRealCombatStrength}.")
                if (realCombatStrength > mRealCombatStrength):
                    wins += 1
                    print("Hero wins the round")
                else:
                    mWins += 1
                    print("Monster wins the round")

            # program end
            break
