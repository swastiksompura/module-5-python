# # Q15.  Write a Python program to print "Hello" using a string. 

# Define a string
message = "Hello"

# Print the string
print(message)




# ===================================================================================================

# # Write a Python program to allocate a string to a variable and print it. 

# Allocate a string to a variable
greeting = "Welcome to Python programming!"

# Print the string
print(greeting)

# ====================================================================================================

# # Write a Python program to print a string using triple quotes. 

# Using triple quotes to define a multi-line string
message = '''Hello,
This is a string written using
triple quotes in Python.'''

# Print the string
print(message)

# =====================================================================================================

# Write a Python program to access the first character of a string using index value.

# Define a string
my_string = "Hello, Python!"

# Access the first character using index 0
first_char = my_string[0]

# Print the result
print("The first character is:", first_char)


# ======================================================================================================

#  Write a Python program to access the string from the second position onwards using slicing. 

# Define a string
my_string = "Python Programming"

# Slice the string from the second character onward (index 1)
sliced_string = my_string[1:]

# Print the result
print("Sliced string from second position:", sliced_string)



# =====================================================================================================

# Write a Python program to access a string up to the fifth character.

# Define a string
my_string = "Python Programming"

# Slice the string from start to the fifth character (index 0 to 4)
sliced_string = my_string[:5]

# Print the result
print("String up to the fifth character:", sliced_string)

# =====================================================================================================

# Write a Python program to print the substring between index values 1 and 4. 
 
 # Define a string
my_string = "Python Programming"

# Slice from index 1 to 4 (includes 1, 2, 3 — excludes 4)
substring = my_string[1:4]

# Print the result
print("Substring from index 1 to 4:", substring)


# ====================================================================================================

#  Write a Python program to print a string from the last character. 

# Define a string
my_string = "Python Programming"

# Access the last character using index -1
last_char = my_string[-1]

# Print the result
print("The last character is:", last_char)


# ========================================================================================================

# Write a Python program to print every alternate character from the string starting from index 1. 

# Define a string
my_string = "Python Programming"

# Slice from index 1 with a step of 2
alternate_chars = my_string[1::2]

# Print the result
print("Alternate characters from index 1:", alternate_chars)
