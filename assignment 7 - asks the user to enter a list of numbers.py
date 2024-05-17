nums=""
count=0
sum=0
print("\t\t\t\tEnter a list of numbers")
while True:
    nums=eval(input("Type a number [Type 0 to stop]: "))
    if nums>0:
        count+=1
        sum+=nums
        ave=sum/count
    else:
        break

print("\nCount: ", count)
print("Sum: ", sum)
print("Average: ", ave)