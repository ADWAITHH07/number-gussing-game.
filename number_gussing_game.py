import random


lowest_num=1

highest_num=100

answer=random.randint(lowest_num,highest_num)
gussess=0
is_running=True
print("python numbr gussesing game")
print(f"select a number bbetween {lowest_num} and {highest_num}")

while is_running:
    guess=input("enter your guss")
    if guess.isdigit():
        guess=int(guess)
        gussess+=1

        if guess < lowest_num or guess > highest_num:
            print("that number is oout of rangge")
            print(f"please select a number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("too low! try again!")

        elif guess > answer:
            print("too high! try again")

        else:
            print(f"correct! the answer was {answer}")
            print(f"number of guuesses:{gussess}")
            is_running=False
    else:
        print("invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num}")

