import random

maxn = 20
number = random.randint(1, maxn)

print("Welcome to number guessing game!\nGhess only from 1-20")
guess = None
while guess != number:
  try:
    guess = int(input("Your guess: "))
    if guess > maxn:
      print(f"Please guess only from 1-{maxn}")
    elif guess > number:
      print("Your guess is too high")
    elif guess < number:
      print("Your guess is too low")
    else:
      print(f"Congratulations! The number is {number}")
  except ValueError:
    print("Please enter a valid number.")