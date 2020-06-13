import random

secretNumber = random.randint(1, 20)
print("Number between 1 and 20")
guess = 0

for guessesTaken in range(1, 7):
    print("Take a guess")
    try:
        data = input()
        guess = int(data)
    except Exception:
        print("Error!!")
        break

    if guess < secretNumber:
      print("Your guess is low.")
    elif guess > secretNumber:
        print("Your guess id too high.")
    else:
        break

if guess == secretNumber:
    print("Good job! " + str(guessesTaken) + " guesses!")
else:
    print("Nope! Answer is " + str(secretNumber))