from random import randint
num=randint(1,10)

guess=0
while num!=guess:
    guess=eval(input("Guess the number between 1 and 10: "))
    if guess>num:
        print("Too high. Try again.")
    elif guess<num:
        print("Too low, Try again.")
    else:
        print("Congratulations. You got it.")