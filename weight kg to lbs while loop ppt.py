while True:
    weight_kg = eval(input("Enter a weight in kilograms: "))
    if weight_kg < 0:
        print("Invalid entry. Weight must be non-negative.")
        continue
    else:
        break

weight_lb = weight_kg * 2.20462
print("Weight in pounds: ", weight_lb)