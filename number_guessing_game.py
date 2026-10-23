import random

secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("NUMBER GUESSING GAME")
print("Guess a number between 1 and 100.")
print("You have", max_attempts, "attempts.")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number from 1 to 100.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        print("Attempts used:", attempts)
        break
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    print("Attempts left:", max_attempts - attempts)

if attempts == max_attempts and guess != secret_number:
    print("Game over! The number was", secret_number)
