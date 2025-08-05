# Q10. Write a Python program to check if a person is eligible to donate blood using a nested if.

# Input age and weight
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

# Nested if condition to check eligibility
if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood due to low weight.")
else:
    print("You are not eligible to donate blood due to age below 18.")
