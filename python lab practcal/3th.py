# Q3 Write a Python program that demonstrates the correct use of indentation, comments, and 

# variables following PEP 8 guidelines. 

# This program calculates the area of a rectangle using proper indentation and comments

def calculate_area(length, width):
    """
    Calculate and return the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    area = length * width
    return area


def main():
    # Define the length and width of the rectangle
    length = 5.0
    width = 3.5

    # Calculate area using the calculate_area function
    rectangle_area = calculate_area(length, width)

    # Display the result
    print("The area of the rectangle is:", rectangle_area)


# Entry point of the program
if __name__ == "__main__":
    main()
