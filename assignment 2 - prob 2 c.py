power=eval(input("Type the power: "))
digits=eval(input("Type the number of digits you want: "))
answer1=2**power
answer2=answer1 % (10**digits)
print("The last desired number of digits is", answer2)