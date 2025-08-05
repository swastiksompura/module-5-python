# Q12. Print this pattern using nested for loop: 
# markdown 
# Copy code 
# * 
# ** 
# *** 
# **** 
# *****


# Outer loop for number of rows
for i in range(1, 6):  # 1 to 5
    # Inner loop for printing stars
    for j in range(i):
        print("*", end="")
    print()  # Move to next line after each row
