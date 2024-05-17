nums=eval(input("Type how many Fibonacci numbers you want to print: "))
num1, num2=0, 1
i=0
print("\nFibonacci: ")
while i < nums:
    fibo=num1 + num2
    num1=num2
    num2=fibo
    i += 1
    print(num1)