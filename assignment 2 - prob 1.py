import random

num1=round(random.uniform(1,100), 2)
num2=round(random.uniform(1,100), 2)
num3=round(random.uniform(1,100), 2)
num4=round(random.uniform(1,100), 2)
num5=round(random.uniform(1,100), 2)
total=num1+num2+num3+num4+num5
average=total/5
print(num1, "+", num2, "+", num3, "+", num4, "+", num5, "=", total)
print("The average of the numbers is ", round(average, 2), ".", sep="")