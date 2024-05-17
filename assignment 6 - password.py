i=0
while i<5:
    i+=1
    left=5-i
    print("\nUsername: Computer Application")
    ps=input("Password: ")
    if ps!="python":
        print("\nInvalid password.")
        print("You only have", left, "tries left to enter the correct password.")
        if left==0:
            print("\nSorry but you are kicked off of the system.")
    else:
        print("\nSuccessfully logged in!")
        break