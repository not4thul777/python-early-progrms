import random
lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True
print("Python Number Guessing Game ")
print(f"secret number between {lowest_num} and {highest_num} ")
while is_running:
    guess=int(input("Enter your guess: "))
    guesses+=1
    if guess<answer:
        print("Too low! Try again.")
    elif guess>answer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {answer} in {guesses} attempts.")
        is_running=False
else:
    print("Game Over. Thank you for playing!")