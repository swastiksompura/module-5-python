# Q18. Write a Python program that manipulates and prints strings using various string methods. 

# Define a sample string
text = "  hello, Python Programming!  "

# Print original string
print("Original string:", repr(text))

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Capitalize the first letter
print("Capitalize:", text.capitalize())

# Convert to title case (first letter of each word capitalized)
print("Title Case:", text.title())

# Remove leading and trailing spaces
print("Stripped:", text.strip())

# Replace a word
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# Find the position of a word
print("Find 'Programming':", text.find("Programming"))

# Check if string starts with 'hello'
print("Starts with 'hello':", text.strip().startswith("hello"))

# Check if string ends with '!'
print("Ends with '!':", text.strip().endswith("!"))

# Count occurrences of a character
print("Count of 'o':", text.count('o'))
