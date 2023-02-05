import random

userScore = 0
computerScore = 0

for game in range(3, 0, -1):

    print(f"game left : {game}")
    user = input("'r' for rock, 'p' for paper and 's' for scissors : ")
    # an iterable of single-character strings can be swapped for a single string
    computer = random.choice('rps')

    if user != computer:
        #  use 'in' to concisely test a bunch of different possibilities
        if user + computer in ('pr', 'sp', 'rs'):
            userScore += 1
        else:
            computerScore += 1
    # eliminate 'else' that doesn't do anything

    print(f"you({userScore}) : {user} & computer({computerScore}) : {computer}\n")
