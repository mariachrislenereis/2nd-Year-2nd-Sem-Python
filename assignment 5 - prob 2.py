hr=eval(input("Type hour between 1 and 12: "))
ap=eval(input("AM (1) or PM (2)? "))
hrsa=eval(input("How many hours ahead? "))

hrsa+=hr

if  ap==1 and hrsa<12 and hrsa>=1:
    print("\nNew hour: ", hrsa, "am")
elif (ap==1 and hr==12) and (hrsa<=24 and hrsa>12):
    hrsa=hrsa-12
    print("\nNew hour: ", hrsa, "am")
elif ap==1 and (hrsa<=24 and hrsa>=12):
    hrsa=(hrsa-24)+24-12
    print("\nNew hour: ", hrsa, "pm")
elif ap==2 and hrsa<=24 and hrsa>12:
    hrsa=(hrsa-24)+24-12
    print("\nNew hour: ", hrsa, "pm")
elif ap==2 and (hrsa<=12 and hrsa>=1):
    hrsa=(hrsa-24)+24
    print("\nNew hour: ", hrsa, "pm")