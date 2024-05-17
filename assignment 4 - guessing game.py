from random import randint

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game...")
print("The number is ", num)

for i in range(3):
    guess=eval(input("Type your guess number between 1 and 20: "))
    if guess==num:
        print("\nCongratulations, you got it!")
        break
    elif guess!=num:
        print("\nOops wrong! Please try again.")
        
else:        
    print("\nGame over! The number is ", num, ".", sep="")