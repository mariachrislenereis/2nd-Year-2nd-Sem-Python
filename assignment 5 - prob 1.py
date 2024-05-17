from random import randint

print("\n\t\t\tWelcome to the Multiplication Game!")
print("\nGeneral Instructions: This game will provide ten randomly generated multiplication questions for the player to answer. Type the correct answer.")

i=0
score=0

while i<10:
    i+=1
    n1=randint(1,10)
    n2=randint(1,10)
    print("\nQuestion", i,":", n1, "x", n2) 
    q=eval(input("= "))
    ans=n1*n2
    if q==ans:
        print("\nCorrect!")
        score+=1
    else:
        print("\nIncorrect.")
        print("The correct answer is ", ans, ".", sep="")
        
print("\n\nYou got", score, "out of ten.") 
print("\nThank you for participating!")       