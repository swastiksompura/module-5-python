# Q8.  Write a Python program to check if a number is prime using if_else. 

# Get input from the user
num = int(input("Enter a number: "))

# Prime number check
if num <= 1:
    print(f"{num} is not a prime number")
else:
    is_prime = True  # assume it's prime

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
