# Q19.  Write a Python program to apply the map() function to square a list of numbers. 

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() with lambda to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Print the result
print("Original list:", numbers)
print("Squared list:", squared_numbers)
